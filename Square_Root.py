#This python program can be calculate the square root
#Note: change this value for a different result.

num=8
# To take the input from the user.
num = float(input("Enter a number that you can calculate square: "))
num_sqrt = num ** 0.5
print("The square root of {} is  {}".format(num, num_sqrt))
"""
#For real or complex numbers.
import cmath
num=eval(input("Enter a number please: "))
#num= 1+2j format you can enter a name.
num_sqrt = cmath.sqrt(num)
print(num)
print("The square root of {} is {}".format(num, num_sqrt))
"""
