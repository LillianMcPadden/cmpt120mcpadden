# attendanceconference.py

from attendeeapp import AttendeeApp
from attendeeinterface import Interface

def main():
    filename = 'file.txt'
    inter = Interface()
    app = AttendeeApp(inter,filename)
    app.run()

if __name__ == '__main__':
    main()
