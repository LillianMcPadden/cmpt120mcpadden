# program9.24_3.py
# This program gets a string and prints out the first 2 and last two chars

def main():
    #Ask the user for the input string
    input_string= input('Enter the string: ')

    # takes the first two letters and the last two leters
    # of the word and prints it
    print (input_string[0:2] + input_string[-2:]) 

main()
