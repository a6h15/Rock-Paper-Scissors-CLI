import random
import time

def mode_three():
    mode = 3
    while mode > 0:
        comp_win = 0
        player_win = 0

        choice = int(input("Press 1 for choosing rock , 2 for scissor , 3 for paper : "))
        print("Player's choice :")
        if choice == 1:
            print(rock)
        elif choice == 2:
            print(scissors)
        elif choice == 3:
            print(paper)
        else:
            print(f"Invalid input , try entering values b/w 1-3")



        print(f"Computer's choice :")

        list1 = [rock, scissors, paper]
        num = random.randint(0, 2)
        CompChoice = list1[num]
        print(CompChoice)

        # rock section
        if CompChoice == rock and choice == 1:
            print("Its a draw---------------------")
            print("Score stays the same")
        elif CompChoice == rock and choice == 2:
            print("Computer WINS------------------")
            comp_win += 1
            print(f"Comp wins : {comp_win} ---------  Your wins : {player_win}")
        elif CompChoice == rock and choice == 3:
            print("You WIN------------------------")
            player_win += 1
            print(f"Comp wins : {comp_win} ---------  Your wins : {player_win}")

        # scissors section
        if CompChoice == scissors and choice == 1:
            print("You WIN------------------------")
            player_win +=1
            print(f"Comp wins : {comp_win} ---------  Your wins : {player_win}")
        elif CompChoice == scissors and choice == 2:
            print("Its a draw---------------------")
        elif CompChoice == scissors and choice == 3:
            print("Computer WINS------------------")
            comp_win += 1
            print(f"Comp wins : {comp_win} ---------  Your wins : {player_win}")


        # paper section
        if CompChoice == paper and choice == 1:
            print("Computer WINS------------------")
            comp_win += 1
            print(f"Comp wins : {comp_win} ---------  Your wins : {player_win}")
        elif CompChoice == paper and choice == 2:
            print("You WIN------------------------")
            player_win += 1
            print(f"Comp wins : {comp_win} ---------  Your wins : {player_win}")
        elif CompChoice == paper and choice == 3:
            print("Its a draw---------------------")
            print("Score stays the same")

        mode = mode -1


print(f"The end score after 3 rounds is : {comp_win}  /  {player_win}")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



print(" --------------------------------------------- ")
print(r"""                _                                  
 _ __ ___   ___| | __  _ __   __ _ _ __   ___ _ __ 
| '__/ _ \ / __| |/ / | '_ \ / _` | '_ \ / _ \ '__|
| | | (_) | (__|   <  | |_) | (_| | |_) |  __/ |   
|_|  \___/_\___|_|\_\ | .__/ \__,_| .__/ \___|_|   
 ___  ___(_)___ ___  _|_| _ __    |_|              
/ __|/ __| / __/ __|/ _ \| '__|                    
\__ \ (__| \__ \__ \ (_) | |                       
|___/\___|_|___/___/\___/|_|                       """)

print(" --------------------------------------------- ")

print(r"""#        _                                                                             _      
#    ___| |__   ___   ___  ___  ___    __ _  __ _ _ __ ___   ___   _ __ ___   ___   __| | ___ 
#   / __| '_ \ / _ \ / _ \/ __|/ _ \  / _` |/ _` | '_ ` _ \ / _ \ | '_ ` _ \ / _ \ / _` |/ _ \
#  | (__| | | | (_) | (_) \__ \  __/ | (_| | (_| | | | | | |  __/ | | | | | | (_) | (_| |  __/
#   \___|_| |_|\___/ \___/|___/\___|  \__, |\__,_|_| |_| |_|\___| |_| |_| |_|\___/ \__,_|\___|
#                                     |___/                                                   """)

game_mode = str(input("------ Best of three or best of five (three/five): "))

if game_mode == "three":
    mode_three()
    print(f"The end score after 3 rounds is : {comp_win}  /  {player_win}")
elif game_mode == "five":
    mode_five()
    print(f"The end score after 5 rounds is : {comp_win}  /  {player_win}")
