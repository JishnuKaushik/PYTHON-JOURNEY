# KEYPAD

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

# its a 2d tuple

for row in num_pad: 
    for num in row:
        print(num, end=" ")
    print()



