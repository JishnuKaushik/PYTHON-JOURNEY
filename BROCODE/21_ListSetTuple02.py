"""
collection = single "variable" useed to store multiple values.
list = [] ordered and changeable. Duplicates OK
set = {} unordered and immutable, but Add/Remove OK . No duplicates
tuble = () ordered and unchangeable. Duplicates OK. FASTER
"""
#                          TUPLE

fruits = ("apple", "orange", "banana", "coconut")
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))
