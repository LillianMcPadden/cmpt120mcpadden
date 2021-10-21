# gcd.py
# This program finds the GCD of two numbers using this algorithm

def main():
    n = int(input('Enter first number: '))
    m = int(input('Enter second number: '))    
    while m:
        n, m = m, n % m
    print('The GCD is', n)
main()
