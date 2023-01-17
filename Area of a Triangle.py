#If a, b and c are three sides of a triangle. Then,
#s = (a+b+c)/2
#area = √(s(s-a)*(s-b)*(s-c))

#With this code, Python program to find the area of triangel

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

#calculate the semi-perimeter
s=(a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is : {} ".format(area))