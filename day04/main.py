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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_of_moves = [rock, paper, scissor]
computer = random.randint(0, 2)
user = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))

if user >= 0 and user <=2:
    print("You chose: ", list_of_moves[user])

print("Computer chose: ", list_of_moves[computer])

if user == computer:
    print("It's a tie!")
elif user == 1 and computer == 0:    
    print("You win :)")
elif user == 0 and computer == 1:
    print("Computer wins!")
elif user == 1 and computer == 2:
    print("Computer wins")
elif user == 2 and computer == 1:
    print("You win!")
elif user == 0 and computer == 2:
    print("You win")
elif user == 2 and computer == 0:
    print("computer wins")
else:
    print("You picked an invalid number. Computer wins")
