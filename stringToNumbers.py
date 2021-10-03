# stringToNumbers.py
# This function is a list of numbers written as strings, 
# Each entry is modified in the list by converting the string to a number

def toNumbers(strList):
    return [int(i) for i in strList]

print(toNumbers(['1','2','3']))
