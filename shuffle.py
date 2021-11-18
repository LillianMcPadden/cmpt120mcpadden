# shuffle.py

from random import randrange

def shuffle(myList):
    for i in range(1,len(myList)):
        item = myList.pop(randrange(len(myList)))
        myList.append(item)
    return myList
    
def main():
    deck = ['Ace', 2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King']
    print("The shuffled cards shuffled in the following order: ", shuffle(deck))

main()
