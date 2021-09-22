# program9.24_2.py
# This program accepts a quiz score as an input
# and prints out the corresponding grade

def main():
    #Ask the user for the quiz score
    score= int(input('Enter the quiz score received: '))

    if score == 0:
        print("Grade: F")
    if score == 1:
        print("Grade: F")
    if score == 2:
        print("Grade: D")
    if score == 3:
        print("Grade: C")
    if score == 4:
        print("Grade: B")
    if score == 5:
        print("Grade: A")
    
main()
