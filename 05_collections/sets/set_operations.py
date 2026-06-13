"""
collection = single "variable" useed to store multiple values.
list = [] ordered and changeable. Duplicates OK
set = {} unordered and immutable, but Add/Remove OK . No duplicates
tuble = () ordered and unchangeable. Duplicates OK. FASTER
"""

#                    SET ; we can not use indexing over here

fruits = {"apple", "orange", "banana", "coconut"}

print(len(fruits))
print("pineapple" in fruits)
# we cannot change a element but we can add or remove though
fruits.add("pineapple") # adds a element
fruits.remove("apple") # removes a element
fruits.pop() # removes a element randomly
fruits.clear() # clear all
