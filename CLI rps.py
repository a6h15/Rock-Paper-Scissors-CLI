#!/usr/bin/env python3
import random
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

choice = int(input("Press 1 for choosing rock , 2 for scissor , 3 for paper : "))
print("Player's choice :")
if choice == 1:
    print(rock)
if choice == 2:
    print(scissors)
if choice == 3:
    print(paper)

print(f"Computer's choice :")

list1 = [rock, scissors, paper]
num = random.randint(0,2)
CompChoice = list1[num]


if CompChoice == rock and choice == 1:
    print(CompChoice)
    print("Its a draw---------------------")
if CompChoice == rock and choice == 2:
    print(CompChoice)
    print("Computer WINS------------------")
if CompChoice == rock and choice == 3:
    print(CompChoice)
    print("You WIN------------------------")

if CompChoice == scissors and choice == 1:
    print(CompChoice)
    print("You WIN------------------------")
if CompChoice == scissors and choice == 2:
    print(CompChoice)
    print("Its a draw---------------------")
if CompChoice == scissors and choice == 3:
    print(CompChoice)
    print("Computer WINS------------------")

if CompChoice == paper and choice == 1:
    print(CompChoice)
    print("Computer WINS------------------")
if CompChoice == paper and choice == 2:
    print(CompChoice)
    print("You WIN------------------------")
if CompChoice == paper and choice == 3:
    print(CompChoice)
    print("Its a draw---------------------")






