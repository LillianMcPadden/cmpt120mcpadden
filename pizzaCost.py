# pizzaCost.py
# This program calculates the cost per square inch of a circular pizza
# given its diameter and price

import math

def main():
    print('This program calculates the cost per square inch of a circular pizza')
    print()
    diameter = float(input('Enter the diameter of the pizza: '))
    price = float(input('Enter the price of the pizza: '))
    cost = price / (math.pi * (diameter/2) ** 2) 
    
    print('The total cost per inch is: $',round(cost,2))

main()
