# Python Calculator

operator = input("Enter an Operator ( + - * / ) : ")

num1 = float(input(" Enter the 1st no :"))
num2 = float(input("Enter the 2nd no :"))


if operator == "+" :
    print(num1+num2)

elif operator == "-" :
    print(num1-num2)

elif operator == "*" :
    print(round(num1*num2 , 3))

elif operator == "/" :
    print(round(num1/num2 , 3))

else :
    print("Please give correct input")

