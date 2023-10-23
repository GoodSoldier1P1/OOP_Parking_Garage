class ParkingGarage():
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets
        self.available_tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_tickets + 1))
        self.currentTicket = {}

    
    def takeTicket(self):   
        if self.available_tickets:
            self.parkingSpaces.pop()
            ticket_number = self.available_tickets.pop(0)
            self.currentTicket[ticket_number] = {
                'paid':False}
            print("Welcome to the Thieves Parking Garage! There are currently " + str(len(self.parkingSpaces)) + " spaces available. Your ticket number is " + str(ticket_number) + ". Please be mindful and respectful towards others who are also trying to park.")
            print("The first floor is reserved for Veterans and couples who are pregnant.")

        else:
            print("The garage is currently full. Sorry for the inconvenience.")

        
    def payForTicket(self):
        ticket_number = int(input('\nPlease enter your ticket number: '))
        if ticket_number in self.currentTicket:
            pay = input("$5 parking fee. How would you like to pay? (Cash - Credit - Debit - Apple Pay) Changed your mind? Select quit to cancel.").lower()
            while True:
                if pay in ['cash','credit','debit','apple pay']:
                    self.currentTicket[ticket_number]['paid'] = True
                    print('Transaction sucessful! Thank you for choosing us as your trusted garage!')
                    print('Your 15 minute timer before you are required to leave starts now!')
                    break
                elif pay == '':
                    print('Please choose an option above in order to continue parking. Quit to cancel.')
                    break
                elif pay == 'quit':
                    print('We are sorry to see you go. Please take the left lane to exit the garage. Thank you!')
            

    def leaveGarage(self):
        ticket_number = int(input('Please enter your parking space number: '))
        if ticket_number in self.currentTicket:
            if self.currentTicket[ticket_number]['paid']:
                print('Once again, thank you for choosing us as your trusted garage! Have a nice day!')
                self.available_tickets.append(ticket_number)
                self.parkingSpaces.append(self.currentTicket[ticket_number])
                del self.currentTicket[ticket_number]
            else:
                print('Payment not received. Please pay now.')


    def runner(self):
        while True:
            option = input('\nHello welcome to Thieves Parking Garage! Please select one of the following options... Park - Pay - Leave. Quit to exit this screen.').lower()
            if option == 'pay':
                self.payForTicket()
                continue
            elif option == 'park':
                self.takeTicket()
                continue
            elif option == 'leave':
                self.leaveGarage()
            elif option == 'quit':
                break
            else:
                print("Sorry we didn't quite catch that... Try again.")

parker = ParkingGarage(500)
parker.runner()