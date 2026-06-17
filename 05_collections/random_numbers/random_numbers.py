import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number = random.randint(1, 20)     # yha pe 1 to 20 ke bich mei se koi random no output me ayega 
number = random.randint(low, high) # no. ki jagh ham variables bhi dal skte hai
print(number)

option = random.choice(options) # choice a option 
print(option)

random.shuffle(cards) 
print(cards)