foods = []
prices = []
total = 0 

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q" : # you can now use q irrespective of there case either lower or upper.
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOU CART -----")        

for food in foods:
    print(food, end=" ")

for price in prices:
    total = total + price # or total += price
    print()
    print (f"YOur total is : ${total}")
