""" 
For Loops = executes a block of code a fixed no of times.
            you can iterate over a range, string, seq, etc.
"""


for x in reversed(range(1, 11, 3)): #to count backwards we enclose range function in reversed function.And the 3 in right is sused to skip the digit an dprint every third digit
    print(x)
print("HAPPY NEW YEAR!")


credit_card = "1234-5678-9012-3456" 
for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 13:
        continue # can use break to stop whole codinf at 12.
    else:
        print (x)