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
import sys
print("Welcome to the game of Rock Paper Scissors (RPS)!")
users_choice = input("What do you choose? Rock, paper or scissors? ").lower()
alternatives = ["rock", "paper", "scissors"]
#if users_choice not in alternatives:
count = alternatives.count(users_choice)
if count == 0:
  print("You didn't write an expected value, you loose!")
  sys.exit()

index_uc = int(alternatives.index(users_choice))
computers_choice = random.randint(0, 2)

if index_uc == 0:
  print(rock)
elif index_uc == 1:
  print(paper)
elif index_uc == 2:
  print(scissors)

  
print("my choice is:")
if computers_choice == 0:
  print(rock)
elif computers_choice == 1:
  print(paper)
elif computers_choice == 2:
  print(scissors)

if index_uc == computers_choice:
  print("It's a draw. Should we try again?")
elif index_uc == 0 and computers_choice == 1:
  #rock against paper
  print("You loose, I win!")
elif index_uc == 1 and computers_choice == 0:
  #paper against rock
  print("You win! Let's try again?")
elif index_uc == 0 and computers_choice == 2:
  #scissors against rock
  print("You win! Let's try again?")
elif index_uc == 0 and computers_choice == 2:
  #rock against scissors
  print("You win! Let's try again?")
elif index_uc == 2 and computers_choice == 1:
  #scissors against paper
  print("You win! Let's try again?")
elif index_uc == 1 and computers_choice == 2:
  #paper against scissors
  print("You loose, I win!")