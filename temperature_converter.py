# Task 2: Temperature Converter

# take temperature input from user
temp = float(input("Enter the temperature value: "))

# take unit from user (C or F)
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# check if unit is Celsius
if unit == "C":
    # convert Celsius to Fahrenheit
    fahrenheit = (temp * 9/5) + 32
    print("Temperature in Fahrenheit is:", fahrenheit)

# check if unit is Fahrenheit
elif unit == "F":
    # convert Fahrenheit to Celsius
    celsius = (temp - 32) * 5/9
    print("Temperature in Celsius is:", celsius)

# if user enters wrong unit
else:
    print("Invalid unit entered")
