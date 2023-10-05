#Circle function
import math
pi = float(math.pi)

def main():
    r = int(input('Please input a radius: '))
    area = calculateArea(r)
    circumference = calculateCircumference(r)
    print('The area of the circle is: ',area)
    print('The circumference of a circle is: ',circumference)

def calculateArea(r):
    return pi * r * r 
def calculateCircumference(r):
    return 2 * pi * r

main()  