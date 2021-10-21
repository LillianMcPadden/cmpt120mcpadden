# goldbach.py
# this program gets a number from the user, checks to make sure that it is even
# and then finds two prime numbers that add up to the number

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

def main():
    n = int(input("Enter an even number greater than 2: "))
    if n % 2 != 0:
        print('Error.', n, " is not an even number")
    elif n <= 2:
        print('Error.', n, " is not greater than 2.")
    else:
        for i in range(3, n):
            if isPrime(i) == 1:
                for l in range(i,n):
                    if isPrime(l) == 1:
                        if n == (i + l):
                            print(i,"+", l, '=', n)
main()
