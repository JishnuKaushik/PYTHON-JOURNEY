"""Format specifiers = {:flags} format a value based on what flags are inserted.
                                flags are inserted.
.(number)f = round to that many decimal places (fixed point)
:(number) = allocate that many spaces 
:03 = allocate and zero pad that many spaces 
:< = left justify
:> = right justify 
:^ = center allign
:+ = use a plus sign to indicate positive value
:= = place sign to leftmost position 
:  = insert a space before positive numbers
:, = comma separator
"""

price1 = 372398475.14159
price2 = -3249878974.443
price3 = 65453.46

# here f means float, and 1 means no. of decimal place req
# if is write a decimal place greater than in the given value it will print zero 
print(f"Price 1 is ${price1: .1f}")
print(f"Price 2 is ${price2: .1f}")
print(f"Price 3 is ${price3: .6f}")

# to add some space just add no of space req after:
print(f"Price 1 is ${price1: 13}")
print(f"Price 2 is ${price2: 13}")
print(f"Price 3 is ${price3: 13}")

# to add some space just add no of space req after and if u wanna add 0 before the digits just write zero before that no. :
print(f"Price 1 is ${price1: 013}")
print(f"Price 2 is ${price2: 013}")
print(f"Price 3 is ${price3: 013}")

# to make the output left justified use < and then the no.and in similar way > for right justified and ^ for center:
print(f"Price 1 is ${price1: <13}")
print(f"Price 2 is ${price2: <13}")
print(f"Price 3 is ${price3: <13}")

# add + sign for positive values :
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

# to have a 1000 place seperator use , :
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

# you can even add multiple flags here :
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")