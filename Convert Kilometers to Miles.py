# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

#conversion factor
conv_fac = 0.621341

#calculate miles
miles = kilometers * conv_fac
print(" {} kilometers is equal to {} miles. ".format(kilometers, miles))
