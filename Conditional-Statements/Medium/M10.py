player1 = input("Enter Player 1 choice: ")
player2 = input("Enter Player 2 choice: ")

if player1 not in ["rock", "paper", "scissors"] or player2 not in ["rock", "paper", "scissors"]:
    print("Invalid choice")
elif player1 == player2:
    print("Draw")
elif (
    (player1 == "rock" and player2 == "scissors") or
    (player1 == "paper" and player2 == "rock") or
    (player1 == "scissors" and player2 == "paper")
):
    print("Player 1 wins")
else:
    print("Player 2 wins")