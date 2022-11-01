inches_str = input("Inches of rain have falles: ")
inches_int =int(inches_str)
volume = (inches_int/12)*43530
gallons = volume *7.48051945
print(inches_int," in. rain on 1 acre is " , gallons, "gallons")
