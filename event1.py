#### Create Event Class
 
 
class Event:
    eventname = ''
    eventcode = ''
    eventTotalAvaibleSeat = 10
 
    def createEvent(self):
        self.eventname= input("Enter Event Name: ")
        self.eventcode = input("Enter Event Code: ")
        self.eventTotalAvaibleSeat = input("Enter Event Total Availble Seats: ")
        print("\n\n ------> Event Created!")
        
        # Create Event Module
 
def createEvent():
    event = Event()
    event.createEvent()
    saveEventDetails(event)

check = ''
num = 0
while check != 8:
    print("\t\t\t\t-----------------------")
    print("\t\t\t\tEVENT MANAGEMENT SYSTEM")
    print("\t\t\t\t-----------------------")
    print("\tMAIN MENU")
    print("\t1. CREATE EVENTS")
    print("\t2. BOOK TICKET")
    print("\t3. VIEW TICKET")
    print("\t4. VIEW EVENTS")
    print("\t5. SHOW SUMMARY")
    print("\tSelect Your Option (1-5) ")
    check = input()

    if check == '1':
        createEvent()
    elif check == '2':
        bookEventTicket()
    elif check == '3':
        getTicketDetails()
    elif check == '4':
        getEventsDetails()
    elif check == '5':
        getEventsSummary()
