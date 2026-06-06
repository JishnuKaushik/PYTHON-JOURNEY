Unit = input("Is the temperature in Celsius or in Fahrenheit (C\F)? : ")

temperature = float(input("Whats the temperature outside ? : "))

if Unit == "C" :
    temperature = ((temperature * 9/5 ) + 32)
    print(f"Hence the temp in Fahrenheit will be : {temperature}")


elif Unit == "F" :
    temperature = ((temperature - 32) * 5/9)
    print(f"Hence the temp in Celsius will be : {temperature}")

else :
    print("Plz select the correct unit")
