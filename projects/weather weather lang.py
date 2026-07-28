# WASSUP

print(" Weather weather ")
temp = (input("What is the temperature outside? (°C): "))

try: 
    temp = float(temp)
    if temp.is_integer():
        temp = int(temp)
except ValueError:
    temp = temp

valid_numbers = isinstance(temp, (int, float))

while valid_numbers is False:
    print(f"{temp} isn't a number bobo")
    temp = (input("What is the temperature outside? (°C): "))
    try: 
        temp = float(temp)
        if temp.is_integer():
            temp = int(temp)
    except ValueError:
        temp = temp
    valid_numbers = isinstance(temp, (int, float))

print()

if temp >= 35:
    print(f"The temperature is {temp}°C degrees Celcius, or {temp * 9/5 + 32}°F degrees Fahrenheit.")
    print("init pre sa loob ka nalang ng bahay niyo")

if temp < 35 and temp >= 20:
    print(f"The temperature is {temp}°C degrees Celcius, or {temp * 9/5 + 32}°F degrees Fahrenheit.")
    print("saktuhan lang pre ok lang yan") 

if temp < 20:
    print(f"The temperature is {temp}°C degrees Celcius, or {temp * 9/5 + 32}°F degrees Fahrenheit.")
    print("lamig lamigan") 
print()

# Problems Encountered:
"""print(" Weather weather ")
temp = (input("What is the temperature outside? (°C): "))
valid_numbers = isinstance(temp, (int, float))    
# THIS VERY LINE WAS THE PROBLEM, BECAUSE IT WAS PUT BEFORE THE "TRY:", IT MEANS THAT IT WAS ALWAYS FALSE
# SO BY REMOVING IT AND PUTTING IT AFTER THE "TRY:", IT NOW WORKS AS IT FUNCTIONS

try: 
    temp = float(temp)
    if temp.is_integer():
        temp = int(temp)
except ValueError:
    temp = temp

valid_numbers = isinstance(temp, (int, float))""""