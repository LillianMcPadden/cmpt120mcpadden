# syracuse.py
# This program gets a starting value from the user and then prints the
# syracuse sequence for that starting value

# JA: You should do this with a loop
def syracuse(x, list = None):
    if list is None:
        list = []
    if x == 1:
        list.append(x)
        return list
    elif x % 2== 0:
        x = x/ 2
        list.append(x)
        return syracuse(x, list)
    else:
        x = (3 * x) + 1
        list.append(x)
        return syracuse(x, list)
