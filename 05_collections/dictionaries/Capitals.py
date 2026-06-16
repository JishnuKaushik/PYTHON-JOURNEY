# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow",}

# print(dir(capitals)) : it list down all the attributes u can use in dic
# print(help(capitals)) : it gives description of all the attributes u can use in dic.
# print(capitals.get("USA"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China") used to remove a specific key 
# capitals.popitem() used to remove the latest key 
# capitals.clear() 
# print(capitals)

# keys = capitals.keys()
# print(keys)

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")