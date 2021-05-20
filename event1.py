## Book a ticket class

class Ticket:
    name = ''
    email = ''
    event = ''
    reference = 200000

    def bookTicket(self):
        print(type(eventdetails))
        self.name= input("Enter Customer Name: ")
        self.email = input("Enter Customer Email: ")
        file = pathlib.Path("events.data")
        if file.exists():
            infile = open('events.data', 'rb')
            eventdetails = pickle.load(infile)

            self.reference = input("Enter Reference Code(10000 - 50000) : ")
            while True:
                if int(self.reference) <= 10000:
                    print("Warning: Please Enter Valid Reference Code")
                    self.reference = input("Enter Reference Code(10000 - 50000) : ")
                else:
                    break

        for event in eventdetails:
            print("Available Event Code : " + event.eventcode + " Event Name : " + event.eventname)
        infile.close()
        self.event = input("Enter Event Code: ")
    def check(self):
        file = pathlib.Path("tickets.data")
        if file.exists():
            infile = open('tickets.data', 'rb')
            ticketdetails = pickle.load(infile)
            for ticket in ticketdetails:
                if ticket.email == self.email and ticket.event == self.event:
                    return True
            infile.close()


    def gettotalticketcount(self):
        file = pathlib.Path("events.data")
        if file.exists():
            infile = open('events.data', 'rb')
            eventdetails = pickle.load(infile)
            for event in eventdetails:
                if event.eventcode == self.event:
                    return int(event.eventTotalAvaibleSeat)
            infile.close
        else:
            return 0

    def getBookedSeatCount(self):
        file = pathlib.Path("tickets.data")
        counter= 0
        if file.exists():
            infile = open('tickets.data', 'rb')
            ticketdetails = pickle.load(infile)
            for ticket in ticketdetails:
                if ticket.event == self.event:
                    counter = counter + 1
            return int(counter)
        return 0

  ###condition checking
  
    def bookEventTicket():
    ticket = Ticket()
    ticket.bookTicket()
    if ticket.check():
        print("Warning : You Already Book A Seat")

    elif ticket.getBookedSeatCount() >= ticket.gettotalticketcount():
        print("Warning : All Ticket Sold Out")

    else:
        print("Sucess : Ticket Booked!")
        saveTicketDetiails(ticket)



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
