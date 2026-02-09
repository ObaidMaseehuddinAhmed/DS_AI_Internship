
def mul(a,b):
    print(a*b)
    
result=mul(2,4)
print(result)

#global & Local ver 1

X=13

def show_varaible():
    X=20
    print(X)
    
show_varaible()
print(X)

#2

count=0

def increase():
    global count
    count+=1
    
increase()
print(count)
    
#3

import math
import random

print(math.sqrt(6)) 
print(random.randint(2,6))

#.
from math import sqrt 

print(math.sqrt(9))


#task1

def calc_rectangle(length, width):
    area= length * width
    perimeter= 2 *(length+width)
    return area,perimeter 

#calling the unction
calc_rectangle(3, 4)

#input of length and width

length=int(input("Enter the length:"))
width=int(input("Enter the breath:"))

#ssiging the variables
area,perimeter = calc_rectangle (length, width)

#printing the value
print(f"the area of rectangle is {perimeter}" )
print(f"the area of rectangle is {area}")

