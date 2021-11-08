# craps_sim.py

from random import randrange

def roll():
    dice = randrange(1,7)
    return dice

def main():
    count = 0
    rolls = 0
    # JA: The number of simulations should come from the user
    while (count == 0):
        d1 = roll()
        d2 = roll()
        result = d1 + d2
        if result == 2 or result == 3 or result == 12:
            count = count - 1 # JA: This could become negative
            print("You lose, sorry!",d1,d2)
        elif result == 7 or result == 11:
            count = count + 1
            print("Winner!", d1,d2)
        else:
            print("Points: ",d1,d2)
        rolls = rolls + 1

    print('The probability of winning is', (count / rolls))
main()


