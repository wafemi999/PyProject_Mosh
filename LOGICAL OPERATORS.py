#TO COMBINE CONDITIONS: OR AND NOT

has_high_income = True
has_good_credit = False
has_criminal_record = True

if has_high_income and not  has_criminal_record:
    print("Eligible for loan")

#comparison operators
temperature = 30

if temperature > 30:
    print("hot day")
else:
    print("not a hot day")


#exercise

name = "john Smith"
print(len(name))

if len(name) < 3:
    print('name must be at least 3 characters long')
elif len(name) > 50:
    print("Name must be max of 50 characters long")
else:
    print("name looks good")

# Weight converter:
weight = int( input("enter weight:"))
unit = input('is weight (L)lbs or (K)kg:')
if unit.upper() == "L":
    conv = weight * 0.45
    print(f"You are {conv}Kilos")
else:
    conv = weight / 0.45
    print(f"You are {conv}Pounds")

