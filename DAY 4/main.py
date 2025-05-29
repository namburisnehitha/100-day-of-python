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

import random
user_input = input("what do u want to choose for rock press 0 paper press 1 and scissors press 2")
if user_input == "0":
    user_input = rock
elif user_input == "1":
    user_input = paper
elif user_input == "2":
    user_input = scissors
computer_choice = random.choice([rock,paper,scissors])
print(computer_choice)
if user_input == computer_choice:
    print("draw")
elif user_input == rock and computer_choice == paper:
    print("you loose")
elif user_input == rock and computer_choice == scissors:
    print("you win")
elif user_input == paper and computer_choice == rock:
    print("you win")
elif user_input == paper and computer_choice == scissors:
    print("you loose")
elif user_input == scissors and computer_choice == rock:
    print("you loose")
elif user_input == scissors and computer_choice == paper:
    print("you win")