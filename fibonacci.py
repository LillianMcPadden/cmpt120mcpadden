# fibonacci.py
# This program finds the nth term of a fibonacci series

def main():
    n = int(input("Enter the term to find from the Fibonacci series: "))
    print("The " + str(n) + " term of the Fibonacci series is:", fibonacci(n))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    n1 = 1
    n2 = 1
    n3 = 0
    for i in range(n-2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n3
main()
