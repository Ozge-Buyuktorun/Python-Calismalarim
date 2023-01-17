#This program computes roots of a quadratic equation when coefficients a, b and c are known.

#general information about quadratic equation
"""ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0
"""
#The solutions of this quadratic equation is given by:
"""(-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
"""
#solve the quadrat,c equation ax**2+bx+c=0
import cmath    # İmport complex math module
a = int(input("Enter a parameter please: "))
b = int(input("Enter b parameter please: "))
c = int(input("Enter c parameter please: "))

#calculation the discriminant
d = (b**2) - (4*a*c)

#find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)  #negative root
sol2 = (-b+cmath.sqrt(d))/(2*a)   #positive root

print("The solution are {} and {} ".format(sol1, sol2))