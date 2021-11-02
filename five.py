# five.py
# write a program that performs a simulation to estimate the probability of
# rolling five of a kind in a single roll of five six-sided dice

from random import randrange

def roll():
    dice = randrange(1,7)

    return dice

def main():
    count = 0
    rolls = 0
    while (count == 0):
        dice1 = roll()
        dice2 = roll()
        dice3 = roll()
        dice4 = roll()
        dice5 = roll()
        if(dice1 == dice2 and dice1 == dice3 and dice1 == dice4 and dice1 == dice5):
            count = count + 1
        rolls = rolls + 1

    print('the chance of rolling five dice and they are all the same is ', count, 'in', rolls, 'chance')

main()
        
