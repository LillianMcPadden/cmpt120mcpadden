# speeding.py
# This program accepts a speed limit and a clocked speed and either prints
# a message indicating the speed was legal or prints the amount of the fine,
# if the speed is illegal

def main():
    speed_limit = eval(input("Enter the speed limit here: "))
    clocked_speed = eval(input("Enter the clocked speed here: "))
    if clocked_speed >= 90:
        bigfine = 250 + (clocked_speed - speed_limit) * 5
        print('Speeding fine: ', bigfine)
    elif clocked_speed > speed_limit:
        fine = 50 + (clocked_speed - speed_limit) * 5
        print('Speeding fine: ', fine)
    else:
        print('Legal speed, drive safe!')

main()
