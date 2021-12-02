# attendeeapp.py

class Attendee:

    def __init__(self, name, company, state, email):
        self.name = name
        self.company = company
        self.state = state
        self.email = email

    def getName(self):
        return self.name

    def getCompany(self):
        return self.company

    def getState(self):
        return self.state
    
    def getEmail(self):
        return self.email

    def __str__(self):
        return 'Name: ' + self.name + '\n' + \
               'Email: ' + self.email

class AttendeeApp:
    def __init__(self, interface, filename):
        self.interface = interface
        self.filename = filename

    def choose(self):
        choice = self.interface.choose()
        [self.addAttendee, self.displayInfo, self.deleteAttendee,
         self.allNamesAndEmails, self.stateNamesAndEmails, self.quit][choice-1]()
        if choice != 6:
            return True
        else:
            return False
    
    def addAttendee(self):
        name, company, state, email = self.interface.addAttendee()
        self.attendees.append(Attendee(name,company,state,email))

    def displayInfo(self):
        self.interface.displayInfo(self.attendees)            

    def deleteAttendee(self):
        self.interface.deleteAttendee(self.attendees)            

    def allNamesAndEmails(self):
        self.interface.allNamesAndEmails(self.attendees)            

    def stateNamesAndEmails(self):
        self.interface.stateNamesAndEmails(self.attendees)            

    def quit(self):
        self.interface.quit()

    def load(self):
        try:
            fileObj = open(self.filename, 'r')
        except FileNotFoundError:
                fileObj = open(self.filename, 'w')
                fileObj.close()
                fileObj = open(self.filename, 'r')
        lst = []
        for line in fileObj:
            name, company, state, email = line.split('\t')
            e = rstrip('\n')
            lst.append(Attendee(name, company, state, email))
        fileObj.close()
        return lst

    def save(self):
        filebj = open(slef.filename, 'w')
        wstring = ''
        for person in self.attendees:
            for function in [person.getName, person.getCompany, person.getState, person.getEmail]:
                wstring = function() + '\t'
                wstring = wstring[:-1] + '\n'
        fileObj.write(wstring[:-1])
        fileObj.close()

    def run(self):
        self.attendees = self.load()
        cont = True
        while cont:
            self.interface.menu()
            cont = self.choose()
        self.save()
