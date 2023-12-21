print("Welcome To The Game of Rock Paper Scissors!")
print(" ")
print("Enter r for Rock, p for Paper and s for Scissors.")
print(" ")

playername1 = input("Enter your name Player1: ")
playername2 = input("Enter your name Player2: ")
n = int(input("Enter the number of rounds you want to play: "))

player1_wins = 0
player2_wins = 0

for round in range(1, n + 1):
  print("")
  print("Round", round, ":")
  player1 = input(playername1 + " Enter your choice: ")
  player2 = input(playername2 + " Enter your choice: ")

  if (player1 == "r" or player1 == "p" or player1 == "s") and \
     (player2 == "r" or player2 == "p" or player2 == "s"):
    if (player1 == "r" and player2 == "s") or \
       (player1 == "p" and player2 == "r") or \
       (player1 == "s" and player2 == "p"):
      print(playername1 + " wins this round!")
      player1_wins += 1
    elif player1 == player2:
      print("It's a tie in this round!")
    else:
      print(playername2 + " wins this round!")
      player2_wins += 1
  else:
    print("Invalid Input (Read the Instructions Again)")
print("")
print("Game Over!")

if player1_wins > player2_wins:
  print("Congratulations, ", playername1, "wins the game!")

elif player1_wins < player2_wins:
  print("Congratulations, ", playername2, "wins the game!")

else:
  print("Game End - 'Its a Tie'")
