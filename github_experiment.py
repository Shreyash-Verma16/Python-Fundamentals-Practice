
import subprocess
import time
from datetime import datetime
from pathlib import Path

FILE = Path("automation_test.txt")
WAIT_SECONDS = 3600  # 1 hour


def git(*args):
    subprocess.run(["git", *args], check=True)


def commit_and_push(message):
    git("add", str(FILE))
    git("commit", "-m", message)
    git("push", "origin", "HEAD")


try:
    # Remember original file state
    existed = FILE.exists()
    original_content = FILE.read_bytes() if existed else None

    # Make a change
    FILE.write_text(
        f"Automated experiment: {datetime.now().isoformat()}\n",
        encoding="utf-8"
    )

    commit_and_push("test: automated temporary change")
    print("Change pushed. Waiting 1 hour...")

    time.sleep(WAIT_SECONDS)

    # Restore original state
    if existed:
        FILE.write_bytes(original_content)
    else:
        FILE.unlink(missing_ok=True)

    # Undo by creating a new commit
    if existed:
        git("add", str(FILE))
    else:
        git("rm", "--cached", "--ignore-unmatch", str(FILE))

    git("commit", "-m", "test: revert automated experiment")
    git("push", "origin", "HEAD")

    print("Original file state restored and undo pushed.")

except Exception as e:
    print("Stopped:", e)
    print("Inspect your repository before retrying.")
