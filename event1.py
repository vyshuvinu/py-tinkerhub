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