# attendeeinterface.py

from attendeeapp import Attendee

class Interface:

    def menu(self):
        print('\nMenu: ')
        print('(1) Add an attendee')
        print('(2) Display information on an attendee')
        print('(3) Delete an attendee')
        print('(4) List all attendees')
        print('(5) List all attendees from a specific state')
        print('(6) Quit')

    def choose(self):
        choice = eval(input('\nSelect 1-5: '))
        return choice

    def addAttendee(self):
        name = input("\nEnter the attendee's name: ")
        company = input('nEnter ' + name + '\'s company: ')
        state = input('nEnter ' + name + '\'s state: ')
        email = input('nEnter ' + name + '\'s email: ')
        print('\nAdded to roster', name)
        return name, company, state, email

    def displayInfo(self, lst):
        name = input('\nEnter the attendees\'s name: ')
        found = False
        for person in lst:
            if person.getName() == name:
                found = True
                personObj = person
                break
        if found:
            print()
            print(personObj)
        else:
            print('\nAttendee not found')

    def deleteAttendee(self,lst):
        name = input('\nEnter the attendees\'s name: ')
        found = False
        for person in lst:
            if person.getName() == name:
                found = True
                del lst[lst.index(person)]
                break
        if found:
            print()
            print(name, 'successfully deleted from attendee list')
        else:
            print('\nAttendee not found')
            
    def allNamesAndEmails(self, lst):
        print('\n{0:<15}     {1:<}'.format('Attendee', 'Email'))
        for p in lst:
            print('\n{0:<15}     {1:<}'.format(p.getName(),p.getEmail()))

    def stateNamesAndEmails(self, lst):
        state = input('\nEnter the full name of the state: ')
        print('\n{0:<15}     {1:<}'.format('Attendee', 'Email'))
        for p in lst:
            if p.getState() == state:
                print('\n{0:<15}     {1:<}'.format(p.getName(),p.getEmail()))

    def quit(self):
        print('\nGoodbye')
