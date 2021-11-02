# craps_sim.py

from random import randrange

def roll():
    dice = randrange(1,7)
    return dice

def main():
    d1 = roll()
    d2 = roll()
    result = d1 + d2
    
    # check if its a win
    if result == 7 or result == 11:
        print("Winner!", d1,d2)
    elif result == 2 or result == 3 or result == 12:
        print("You lose, sorry!",d1,d2)
    else:
        print("Points: ",result, d1,d2)
main()


