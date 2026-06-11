"""
nested loops = a loop within another loop (outter, inner)
                outer loop:
                    inner loop:
"""
for y in range(3):
    for x in range(1, 10):
        print(x, end="")
    print()    