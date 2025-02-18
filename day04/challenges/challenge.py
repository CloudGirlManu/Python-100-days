import random

friends = ["Alice", "Bob", "Jeremiah", "Manuela", "Chiemerie"]

#Method1
print(random.choice(friends))

#Method2
random_friends = random.randint(0, 4)
print(friends[random_friends])