# CALCULATOR PROGRAM!@!

print()
print("Hello, first try manually coding a calculator\nwith the help of claude ai in whic i used only for correcting errors")
print("and also brocode 12hour python vidfeo yung nasa 1hr mark\nokbye")
print()

operator = input("Enter an operator (+ - * /): ")
valid_operators = ("+", "-", "*", "/")
while operator == "":
    print("enter an operator bro wtf")
    operator = input("Enter an operator (+ - * /): ")
while operator not in valid_operators:
    print(f"bobo, {operator} isn't valid operator! Try again.")
    operator = input("Enter an operator (+ - * /): ")

print(f"You entered: {operator}")
print()
print("Great! now pick a number")

#######################################
num_1 = input("Enter a number: ")
while num_1 == "":
    print("enter a number bro wtf")
    num_1 = (input("Enter a number: "))
    valid_numbers = isinstance(num_1, (int, float))
try:                                                    # THIS WHOLE LINE IS TO TRY TO MAKE SURE THAT WHEN A STRING IS INPUTED, IT IS INVALIDATED
    num_1 = float(num_1)                                # AND SO THAT ONLY INTEGERS AND FLOAT NUMBERS ARE THE TEXTS ACCEPTED IN THE THING
    if num_1.is_integer():
        num_1 = int(num_1)
except ValueError:
    num_1 = num_1
valid_numbers = isinstance(num_1, (int, float))
while valid_numbers is False:
    print(f"{num_1} isn't a number bro, try again")
    num_1 = (input("Enter a number: "))
    try:
        num_1 = float(num_1)
        if num_1.is_integer():
            num_1 = int(num_1)
    except ValueError:
        num_1 = num_1
    valid_numbers = isinstance(num_1, (int, float))

print(f"You entered: {num_1}")
print()
print("Great! now pick another number")

#######################################
num_2 = input("Enter the second number: ")
while num_2 == "":
    print("enter a number bro wtf")
    num_2 = (input("Enter a number: "))
    valid_numbers = isinstance(num_2, (int, float))
try:                                                     # THIS WHOLE LINE IS TO TRY TO MAKE SURE THAT WHEN A STRING IS INPUTED, IT IS INVALIDATED
    num_2 = float(num_2)                                 # AND SO THAT ONLY INTEGERS AND FLOAT NUMBERS ARE THE TEXTS ACCEPTED IN THE THING
    if num_2.is_integer():
        num_2 = int(num_2)
except ValueError:
    num_2 = num_2
valid_numbers = isinstance(num_2, (int, float))
while valid_numbers is False:
    print(f"{num_2} isn't a number bro, try again")
    num_2 = (input("Enter a number: "))
    try:
        num_2 = float(num_2)
        if num_2.is_integer():
            num_2 = int(num_2)
    except ValueError:
        num_2 = num_2
    valid_numbers = isinstance(num_2, (int, float))

print(f"You entered: {num_2}")
print()
print("eto na sagot mo lol")

if operator == "+":
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
    print(f"Total: {num_1 + num_2:,}")
if operator == "-":
    print(f"{num_1} - {num_2} = {num_1 - num_2}")
    print(f"Total: {num_1 - num_2:,}")
if operator == "/":
    print(f"{num_1} / {num_2} = {num_1 / num_2}")
    print(f"Total: {num_1 / num_2:,} OR {round(num_1 / num_2, 2):,}")
if operator == "*":
    print(f"{num_1} * {num_2} = {num_1 * num_2}")
    print(f"Total: {num_1 * num_2:,}")


## Kind of learned all this through Claude AI ,laki ng tulong grabe hayup leeg ang tama
## Errors encountered: dami hahah

# try:
# except ValueError:
#     num_2 = num_2
# valid_numbers = isinstance(num_2, (int, float))
# while valid_numbers is False:
#     print(f"{num_2} isn't a number bro, try again")
#     num_2 = (input("Enter a number: "))
#     try:
#         num_2 = float(num_2)
#         if num_2.is_integer():
#             num_2 = int(num_2)
#     except ValueError:
#         num_2 = num_2
#     valid_numbers = isinstance(num_2, (int, float))

## this code is learnt through AI: nagprompt ako nung kung paano i-classify yung num_1 as an integer and a float
## and also kung paano siya i-invalidate pag string ang user input
## tangina hirap w



