weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K" or unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit} ")
elif unit == "L" or unit == "l":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit} ")
else:
    print(f"{unit} was not valid. Please enter 'K' or 'k' for Kilograms and 'L' or 'l' for Pounds.")

