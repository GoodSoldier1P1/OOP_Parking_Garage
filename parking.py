class ParkingGarage():
    def __init__(self) -> None:
        spots = 400
        self.tickets = [1] * spots
        self.parkingSpaces = [1] * spots
        self.currentTicket = {'paid': 'False'}

    
    def takeTicket(self):
        print("Thank you for choosing the Thieves Parking Garage! Tickets are $10 and to be paid as you exit the garage.")
        print("There are " + str(len(self.tickets)) + " tickets available")
        print("There are " + str(len(self.parkingSpaces)) + " spaces available")
        print("The first floor is reserved for Veterans and couples who are pregnant.")
        self.tickets.pop()
        self.parkingSpaces.pop()


    def payForTicket(self):
        paid = input("Please enter ticket ammount. (ex. 10). Please enter 'Vet' if you are a Veteran. Please have MID ready.").lower() # The terminal can't scan the Military ID so we will pretend this part happens
        while True:
            if paid == '':
                print("Please enter a valid ammount.")
                break
            elif paid == 'vet':
                print("Thank you for your service and dedication. Parking Fee is on us.")
                self.currentTicket['paid'] = 'True'
                break
            else:
                print("Thank you for using the Thieves Parking Garage!")
                print("-----Fine Print-----")
                print("If ticket holder does not exit within 15 minutes, ticket must be paid again.")
                self.currentTicket['paid'] = 'True'
                break


    def leaveGarage(self):
        for v in self.currentTicket.values():
            if v == 'True':
                print("Ticket has been paid. Thank you for using Thieves Parking Garage!")
                print('\nThere are ' + str(len(self.tickets)) + ' tickets available')
                print('\nThere are ' + str(len(self.parkingSpaces)) + ' spaces available')
                self.tickets.append(1)
                self.parkingSpaces.append(1)
                self.currentTicket['paid'] = 'False'
                
            else:
                print("Ticket has not been paid, please enter Paying option.")
                pass


    def runner(self):
        while True:
            choice = input("Ticket must be paid before exiting the garage. Are you parking, leaving or paying? (Parking / Leaving / Paying. Quit to exit)").lower()
            if choice == 'paying':
                self.payForTicket()
                continue
            elif choice == 'parking':
                self.takeTicket()
                continue
            elif choice == 'leaving':
                self.leaveGarage()
                continue
            elif choice == 'quit':
                break


parker = ParkingGarage()
parker.runner()
