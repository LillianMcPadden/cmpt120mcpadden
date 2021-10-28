# logic_gates.py

def and_g(a,b):
    if a == 0 or b == 0:
        return 0
    else:
        return 1

def or_g(a,b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0

def not_g(a):
    if a == 1:
        return 0
    else:
        return 1

def nand_g(a,b):
    if a == 0 or b == 0:
        return 1
    else:
        return 0

def xor_g(a,b):
    if (a == 0 and b == 0) or (a == 1 and b == 1):
        return 0
    else:
        return 1

def main():
    a = int(input("enter a number (a) either 0 or 1: "))
    b = int(input('enter a number (b) either 0 or 1: '))
    print('And: ', and_g(a,b))
    print('Or: ', or_g(a,b))
    print('Not', not_g(a))
    print('Nand', nand_g(a,b))
    print('Xor', xor_g(a,b))
