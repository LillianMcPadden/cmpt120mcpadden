# program9.24_1.py
# This program gets a string from a given string where all occurences of its
# first char have been changed to $ except for the first char itself

def main():
    #Ask the user for a string
    string= input('Enter a string: ')

    char = string[0]
    string = string.replace(char, "$")
    string = char + string[1:]
    print(string)
    
main()
