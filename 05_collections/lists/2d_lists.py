fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries =[fruits, vegetables, meats]

print(groceries[0][0])
# if we will use single index it will print whole raw.
# thats why we use two index it works as co-ordinates.

# Another way of doing it is 

groceries = [["chicken", "fish", "turkey"], 
             ["celery", "carrots", "potatoes"], 
             ["apple", "orange", "banana", "coconut"]]

# u can add tuple in ste set in tuple list in tuple etc

for collection in groceries :
    for food in collection :
        print (food, end=" ") # this will ad space bw all elements
    print() #its for the new line for each list     