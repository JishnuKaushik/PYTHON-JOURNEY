# input = A function that prompts the user to enter data
#         Returns the entered data as a string.

name = input("what is your name ?: ")
age = int(input("what is your age ?: ")) # why we used type casting here ?? this is because when we take input from user that data is returned in form of str()

age = age + 1  # as we typcasted the age from str() to int now we will be able to do arithmetic operations on it.

print(f"hello, {name}")
print(f"yo bitch {age}")
