
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("You are at a crossroad. Where do you want to go?")
direction = input('Welcome to Treasure Island! '
                  'Your mission is to find the treasure. '
                  'You are at a crossroad. Where do you want to go? '
                  'Type \"left\" or \"right\" ').lower() #We can use lower() function or we can use logical operators
if direction == "left":
    lake_action = input('You have come to a lake. There is an island in the middle of the lake. '
                        'Type \"wait\" to wait for a boat. Type \"swim\" to swim across ').lower()
    if lake_action == "swim":
        door = input('You have reached the island. There are 3 doors in front of you '
                     'Choose the color of the door you want to go through '
                     'Type \"yellow\", \"green\" or \"red\" ').lower()
        if door == "red":
            print("Congratulations! You made it!")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************

''')
        else:
            print("Oh no! There are snakes behind this door. You lost!")
    else:
        print("You have drowned and died! Better luck next time!")
else:
    print("You fell into a hole and died xo Game over!!!")
