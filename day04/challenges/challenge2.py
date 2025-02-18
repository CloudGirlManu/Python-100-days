# There are different ways to achieve the Heads or Tails game.
# To run this script comment one section to run the other
import random


#Method1
random_game = random.choice(['Heads', 'Tails'])
print(random_game)

#Method2
random_number = random.randint(1, 2)
if random_number == 1:
    print("Heads")
else:
    print("Tails")
