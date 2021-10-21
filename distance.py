# distance.py
# This program determines the distance to a lightning strike based on the
# time elapsed between the flash and the sound of thunder

def main():
    speed_of_sound = 1100 #ft per sec
    one_mile = 5280 #ft

    print('This program determines the distance of a lightning strike')
    time = float(input('Enter the time elapsed in seconds between the flash and the ' + \
                       'sound of thunder: '))
    distance = speed_of_sound * time
    miles = distance // one_mile
    feet = distance % one_mile

    print('The distance to the lightning strike is ', miles, 'miles and', + \
          feet, 'feet from your current location.')

main()
