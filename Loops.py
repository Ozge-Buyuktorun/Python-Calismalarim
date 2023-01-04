"""fruits = ["apple", "orange","pears", "cherries","grapes"]

for i in fruits:
    print("Would you like {} ?".format(i))

for number in range(1,11):
    print(" Number : {}".format(number))

import time

temp_f = 40
while temp_f > 32:
    print("The water is {} degress.".format(temp_f))
    time.sleep(1)
    temp_f -= 1
    if temp_f == 33:
        break
for number in range (1,11):
    if number ==7:
        print("We're skipping number 7")
        continue
    print("This is the number {}.".format(number))

for number in range (1,11):
    if number ==3:
        pass
    else:
        print("This is the number {}.".format(number))
"""
