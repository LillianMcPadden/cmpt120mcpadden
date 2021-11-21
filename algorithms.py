# algorithms.py

def count(myList, x):
    return myList.count(x) # JA: You were not supposed to use these functions

def isin(myList, x):
    if myList.count(x) > 0:
        return True
    else:
        return False
    
def index(myList, x):
    return myList.index(x)

def reverse(myList):
    myList.reverse()
    return myList

def sort(myList):
    myList.sort()
    return myList

def main():
    lst = [1,2,25,17,3,4,4,5,6,9,47,38,9]
    print('Count (4): ', count(lst,4))
    print('Is in (2): ', isin(lst,2))
    print('Index (3): ', index(lst,3))
    print('reverse list: ', reverse(lst))
    print('sort list: ', sort(lst))

main()
