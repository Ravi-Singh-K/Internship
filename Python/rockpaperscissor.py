

# import random

# information = {'R':"Rock", 'P':"Paper", 'S':"Scissor"}
# choices = ['R','P','S']
# close = False

# while not close:
#     player = input("Please choose your move . ['R' for Rock, 'P' for Paper and 'S' for Scissor] ['Q' to Quit the game]")
#     computer = random.choice(choices)
#     if player == computer:
#         print(f"Computer choosed {computer}")
#         print("It's a tie.")
#     elif player == 'R' and computer == 'P':
#         print(f"Computer choosed {computer}")
#         print("Computer Wins")
#     elif player == 'P' and computer == 'S':
#         print(f"Computer choosed {computer}")
#         print("Computer Wins")
#     elif player == 'S' and computer == 'R':
#         print(f"Computer choosed {computer}")
#         print("Computer Wins")
#     elif player == 'Q':
#         close = True
#     else:
#         print(f"Computer choosed {computer}")
#         print("Player Wins")