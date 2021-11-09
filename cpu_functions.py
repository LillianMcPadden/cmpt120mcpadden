# cpu_functions.py
from logic_gates import * 

def one_bit_adder(a,b,ci):
    # if a + b + ci == 0:
    #     sumb = 0
    #     co = 0
    #     print('sum: ', sumb,
    #           'co: ', co)
    # elif a + b + ci == 1:
    #     sumb = 1
    #     co = 0
    #     print('sum: ', sumb,
    #           'co: ', co)
    # elif a + b + ci == 2:
    #     sumb = 0
    #     co = 1
    #     print('sum: ', sumb,
    #           'co: ', co)
    # else:
    #     sumb = 1
    #     co = 1
    #     print('sum: ', sumb,
    #           'co: ', co)
    xor_t = xor_g(a,b)
    sumb = xor_g(xor_t,ci)
    and_1 = and_g(xor_t,ci)
    and_2 = and_g(a,b)
    co = or_g(and_1,and_2)
    return sumb, co

def main():
    a = int(input('Enter a number (a) either 0 or 1: '))
    b = int(input('Enter a number (b) either 0 or 1: '))
    ci = int(input('Enter a number (ci) either 0 or 1: '))
    one_bit_adder(a,b,ci)

main()
