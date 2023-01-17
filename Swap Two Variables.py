# Python program to swap two variables
"""
x = input("Enter value of x: ")
y = input("Enter value of y: ")

#create a temporary variable and swap the values.
temp = x
x = y
y = temp

print(" The value of x after swagging : {} ".format(x))
print(" The value of y after swagging: {} ".format(y))
"""
# Without Using any Temporary Variable, we can swat two variables:
x = 5
y = 20

x, y = y ,x
print("x = ",format(x))
print("y = ",format(y))