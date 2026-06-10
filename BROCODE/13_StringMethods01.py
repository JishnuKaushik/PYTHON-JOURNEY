#validate user input exercise 
# 1. username is no more than 12 characters.
# 2. user name must not contain spaces.
# 3. user name must not contain digits.


username = input("enter a username")

if len(username) > 12 :
    print ("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print ("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else: 
    print(f"Welcome {username}")