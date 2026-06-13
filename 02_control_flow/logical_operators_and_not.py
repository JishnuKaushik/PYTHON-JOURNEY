"""Logical Operator = Evaluate multiple conditions (or, and, not)
                    or = atleast one condition must be true
                    and = both conditions must be true.
                    not = inverts the condition (not false , not ture)
"""
#  and & not
temp = 25
is_sunny = False
if temp >= 28 and is_sunny:
    print("It is Hot outside")
    print("It is Sunny Leone")

elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is Sunny ")

elif 28 > temp > 0  and is_sunny:
    print("It is warm outside")
    print("It is Sunny ")

if temp >= 28 and not is_sunny:
    print("It is Hot outside")
    print("It is cloudy")

elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")

elif 28 > temp > 0  and not is_sunny:
    print("It is warm outside")
    print("It is cloudy")