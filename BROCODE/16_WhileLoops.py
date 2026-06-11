# While Loop = execute some code WHILE some conditions remains true.

name = input("Enter your name : ")
age = int(input("Enter your age : "))


while name  == "":
    print("You did not enter your name")
    name = input("Enter your name : ")

while age < 0 :
    print("Age cant be negative")
    age = int(input("Enter your age : "))

print(f"hello {name}")
print(f"hello your age is : {age}")