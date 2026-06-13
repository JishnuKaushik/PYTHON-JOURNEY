"""Logical Operator = Evaluate multiple conditions (or, and, not)
                    or = atleast one condition must be true
                    and = both conditions must be true.
                    not = inverts the condition (not false , not ture)
"""
#  or
Mausam = input("Bahar mausam kese hai? :")
Is_Ground_occupied = False

if Mausam == "kharab" or Is_Ground_occupied :
    print("Aj nhi khelenge")
else : 
    print("chalo khelne chale" )