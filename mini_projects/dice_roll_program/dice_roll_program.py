import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") # code to print characters we need to create dice.
# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

# a dictionary made out of key : value pairs here value is a tuple made of struings and each key is a no.
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│    ●    │",
        "│         │",
        "│    ●    │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│    ●    │",
        "│    ●    │",
        "│    ●    │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")   
}

dice = []
total = 0
num_of_dice = int(input("How many dice? : "))

for die in range (num_of_dice):
    dice.append(random.randint(1, 6))

#for die in range (num_of_dice):
#    for line in dice_art.get(dice[die]): # here die works as the index
#            print(line)

# to print dice art in a single line use this instead:

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")    

