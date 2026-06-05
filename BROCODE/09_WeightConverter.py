# Python Weight Converter

weight = float(input("enter your weight: "))
unit = input(" kilograms or pounds ? :")

if unit == "K" :
    weight = weight * 2.205
    unit = "LBS."

elif unit == "L" :
    weight = weight / 2.205
    unit = "KGS."

else : 
    print (f"{unit} was not valid" )

print(f"Your weight is : {weight} {unit}")    
