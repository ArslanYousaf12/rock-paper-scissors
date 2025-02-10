import random as r
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
    # Rules
    # Rock = 0
    # Paper = 1
    # Scissors = 2
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.


#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = r.randint(0,2)
if user_choice == 0 and computer_choice == 2:
  print(f"You chose:\n{rock}")
  print(f"Computer chose:\n{scissors}")
  print("You win!")
elif user_choice == 2 and computer_choice == 1:
  print(f"You chose:\n{scissors}")
  print(f"Computer chose:\n{paper}")
  print("You win!")
elif user_choice == 1 and computer_choice == 0:
  print(f"You chose:\n{paper}")
  print(f"Computer chose:\n{rock}")
  print("You win!")
elif user_choice == computer_choice:
  if user_choice == 0:
    print(f"You chose:\n{rock}")
    print(f"Computer chose:\n{rock}")
  elif user_choice == 1:
    print(f"You chose:\n{paper}")
    print(f"Computer chose:\n{paper}")
  else:
    print(f"You chose:\n{scissors}")
    print(f"Computer chose:\n{scissors}")
  print("It's a draw!")
else:
  print(f"You chose:\n{rock if user_choice == 0 else paper if user_choice == 1 else scissors}")
  print(f"Computer chose:\n{rock if computer_choice == 0 else paper if computer_choice == 1 else scissors}")
  print("You lose!")


