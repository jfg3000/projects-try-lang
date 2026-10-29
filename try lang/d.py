#interchange of variables

"""# start
input var1, var2
SET tempvar = var1
set var1 = var2
set var2 = tempvar
print var1, var2 
# END"""

temp = "goood"
something = "bad"
print (temp, something)

temp1 = temp
temp = something
something = temp1

print (temp, something)

problem2

start 
input num1, num2, num3
if num1 >= num2 and num1 >= num3:
    print ("num1 is the largest number")
elif num2 >= num1 and num2 >= num3:
    print ("num2 is the largest number")
else:
    print ("num3 is the largest number")
end if
end 

start 
input num1, num2, num3
set greatest = num1
if num2 >= greatest:
    set greatest = num2
eliif num3 >= greatest:
    set greatest = num3
print (greatest, "is the largest number")
end if 
end 


problem3

start 
input call
if call <= 300:
    set bill = 500 # 500 IS FIXED FOR THE FIRST 300 CALLS 
elif call <= 365:
    set bill = 500 + 9.50 * (call - 300) # 500 + 9.50 * 65 = 500 + 617.5 = 1117.5
elif call <= 455:
    set bill  = 1117.5 + 15 * (call - 365) # 1117.5 + 15 * 90 = 1117.5 + 1350 = 2467.5
else:
    set bill = 2467.5 + 22.50 * (call - 455) # 2467.5 + 22.50 * 45 = 2467.5 + 1012.5 = 3480
endif 
print bill
end 

problem4 Devise a procedure to find the sum of the first n natural numbers, where n is any given integer, without using a formula.

start 
input n
set sum = 0 
set number = 1
is number <= n?
while number <= n ( if yes )
    set number = number + 1 
    set sum = sum + number   
is number <= 0? ( if no )
print sum
end






