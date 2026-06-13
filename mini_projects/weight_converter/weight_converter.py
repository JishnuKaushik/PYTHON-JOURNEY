# Python Weight Converter

weight = float(input("enter your weight: "))
unit = input(" kilograms or pounds ? :")

if unit == "K" :
    weight = weight * 2.205
    unit = "LBS."
    print(f"Your weight is : {weight} {unit}")

elif unit == "L" :
    weight = weight / 2.205
    unit = "KGS."
    print(f"Your weight is : {weight} {unit}")

else : 
    print (f"{unit} was not valid" )

    
