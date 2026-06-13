"""
collection = single "variable" useed to store multiple values.
list = [] ordered and changeable. Duplicates OK
set = {} unordered and immutable, but Add/Remove OK . No duplicates
tuble = () ordered and unchangeable. Duplicates OK. FASTER
"""
#                       LIST :-

fruits = ["apple" , "orange" , "banana" , "guvava"]

print(fruits[0]) 
# {#basically u can use index operaters over here like step ::n, reverse : -1 ,etc.}

for fruit in fruits:
    print(fruit)
#general convention ke acc for loop mei x ki jagh singular use karte hai and jis range ya list ke elements ke sath deal kr rhe hai use plural.

print(len(fruits))
print("apple" in fruits)# boolean
fruits[0] = "pineapple" #we can replace a value using index.
fruits.append("pineapple") # add
fruits.insert(0, "pineapple")
fruits.sort() # alphabatical order
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count("banana"))
