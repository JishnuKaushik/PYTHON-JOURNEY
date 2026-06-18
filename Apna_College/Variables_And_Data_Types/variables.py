# A variable is a name given to a memory location in a program.
# "=" assignment operator
# rules for identifiers =>
"""
1. Identifiers can be combination of upper case and lower case letter, digits or an underscore(_).
2. An identifiers can not start with digit. so while variable1 is valid, 1variable is not valid.
3. we can't use special symbols in our identifiers.
4. Identifiers can be aof any length.
"""

name = "Jishnu Kaushik" # string
age = 18
dob = "16/11/2007"

age2 = age

# instead of using f strings which i was using up until now i can also use :
# format = print("string", variable)

print("my name is : ", name)
print("my age and dob is :", age , dob)

print (age2)