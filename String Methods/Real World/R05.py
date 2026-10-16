note = "SAVE10 applied; customer asked about SAVE10"
code = "SAVE10"

count = note.count(code)
index = note.find(code)

if index != -1:
    print("Count:", count)
    print("First index:", index)

    updated_note = note.replace(code, "[CODE APPLIED]")
    print(updated_note)
else:
    print("Code not found")
