# Loooops 
# For loops


from ast import For

for i in range(3, 100, 3):
    print(i, end=", ")
    
print()

### hirap neto GAGO #######

num_count1 = []
for number in range(2,21,1):
    num_count1.append(number)
print(num_count1)

num_count2 = []
for number in range(2,21,1):
    num_count2.append(number)
    print(num_count2)    # if its indented, it prints until it runs out of variables to print or the multiples ended

num_count3 = []
for number in range(2,21,1):
    squared = number ** 2 
    num_count3.append(squared)
print(num_count3)        # if not indented, it only prints all values in one print 