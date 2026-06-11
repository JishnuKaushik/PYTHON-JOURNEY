"""
nested loops = a loop within another loop (outter, inner)
                outer loop:
                    inner loop:
"""

rows = int(input("enter the no. of rows : "))
columns = int(input("enter the no. of columns : "))
symbol = int(input("enter the symbols to use : "))

for y in range(rows):
    for x in range(columns):
        print(symbol, end="")
    print()