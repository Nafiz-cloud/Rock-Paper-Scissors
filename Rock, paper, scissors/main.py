'''
1 = Rock
0 = Paper
-1 = Scissors

'''

import random 

game_dict  = {
    1 : "Rock",
    0 : "Paper",
    -1 : "Scissors"
}

player = int(input("Enter your choice: "))
print(f"You chose {game_dict[player]}") # {game_dict[1]} and the correspoding of 1 is Rock
computer = random.choice([-1, 0, 1])
print(f"Computer chose {game_dict[computer]}")

if player == computer:
    print("It's a tie!")

else:
    if (player == 1 and computer == 0):
        print("Computer wins!")
    elif (player == 1 and computer == -1):
        print("Player wins!")
    elif (player == 0 and computer == 1):
        print("Player wins!")
    elif (player == 0 and computer == -1):
        print("Computer wins!")
    elif (player == -1 and computer == 1):
        print("Computer wins!")
    elif (player == -1 and computer == 0):
        print("Player wins!")
    else:
        print("Invalid input! Please enter 1, 0, or -1.")
    