# Randomie
# This is the simple script that generate random numbers
# Just choose a size of number, its type (integer or fractional) and this script will automatically generate a random number

import random

person_type = (input("Type a kind of a number - integer or fractional: "))
person_from = (input("Type a range 'from' of a random number: "))
person_to = (input("Type a range 'to' of a random number: ")) 
if person_type == "integer" or "INTEGER" or "Integer":
    integ_output = random.randint(int(person_from), int(person_to))
    print (integ_output)
if person_type == "fractional" or "Fractional" or "FRACTIONAL":
    frac_output = random.uniform(int(person_from), int(person_to))
    print(frac_output)
else:
    print("Please type a kind of a number correctly(Without any extra characters). Restart the script.")





