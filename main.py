
#* Project Name - Railway Reservation project
#* Author - Rahul
#* Location - Nahan, Himacahl Pradesh
#* Date - 23-07-2022

#! Modules used in Program

import random #* For generating unique ID's and captchas
import time #* For time.sleep() function
from datetime import datetime #* It will give me current date
from datetime import date #* It will give me current time
from tqdm import tqdm #* For the progress bar


class Train:  # *Created a class Train
    # * Opening availableSeats.txt in read mode file from Train Info Folder
    with open('Train Info/availableSeats.txt', 'r') as f:
        availableSeats = f.read()  # * Reading contents of file availableSeats.txt
    # * Opening fare.txt in read mode file from Train Info Folder
    with open('Train Info/fare.txt', 'r') as f:
        fare = f.read()  # * Reading contents of file fare.txt
    #! All properties like train name, seats, fare price, datetime
    TrainName = "GUPTA EXPRESS"
    seats = int(availableSeats)
    Fare = int(fare)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    date = date.today()

    # * Created a constructor that takes parameter uniqueid, destination, captcha
    def __init__(self, uniqueid, destination, captcha):
        self.UniqueID = uniqueid
        self.Destination = destination
        self.captcha = captcha

    # * This function displays the current info of train from files and from constructor
    def train_info(self):
        print(f'''************************ \tTRAIN INFORMATOIN IS SHOWN BELOW ************************
NAME OF THE TRAIN IS: {self.TrainName}
CURRENTLY SEATS AVILABLE IN TRAIN ARE: {self.seats}
FARE FOR 1 TICKET IS: {self.Fare}
DESTINATION: {self.Destination}''')

    def Book_ticket(self):  # * User can book tickets through this function
        bookTicket = int(
            (input("Enter the number of tickets you want to book: ")))  # * Asking user to enter the number of tickets he wants to book
        try:  # * Try statement is added in case program throws an error so that it will not crash
            if bookTicket <= self.seats:  # * IF-Else condition block
                print("Please wait.....")
                time.sleep(1)
                # * Asking user's Name to generate receipt of his name
                userName = input("Enter your name to generate receipt\n")
                # * Creating and Opening a text file in write mode of his name in folder Booked Tickets
                with open(f"Booked Tickets/{userName}.txt", 'w') as f:
                    bookTicketReceipt = (f'''\t******************************* YOUR SEATS ARE BOOKED *******************************
NAME OF THE TRAIN IS: {self.TrainName}
NAME OF RECEIPANT: {userName}
SEATS BOOKED: {bookTicket}
DESTINATION: {self.Destination}
AMOUNT TO PAY: {bookTicket*self.Fare} Rs.
RECEIPT GENERATED ON: {self.date}
TIME OF BOOKING: {self.current_time}
YOUR UNIQUE ID: {self.UniqueID}


USE YOUR UNIQUE ID AT PAYMENT AND TO GET PHYSICAL TICKETS.....


*************************** THANKS FOR USING OUR SERVICE. HAVE A GOOD DAY {userName} ***************************''')
                    f.write(
                        bookTicketReceipt)  # * The content of book tickets is stored in the file of his name
                    # * Deducting the tickets booked by user from our available sets file
                    Train.seats = Train.seats - bookTicket
                    # * Opening avilable seats in read mode
                    with open('Train Info/availableSeats.txt', 'r') as f:
                        f.read()  # * reading the contents
                    # * Opening avilable seats in write mode
                    with open('Train Info/availableSeats.txt', 'w') as f:
                        # * Updating the old seats with seats left after deduction
                        f.write(str(Train.seats))
                    # * Then creating a new file which is named as user's Unique ID in Unique ID's Folder
                    with open(f"Unique ID's/{self.UniqueID}.txt", 'w') as f:
                        # * In first line storing booked tickets by the user
                        f.write(f"{bookTicket}\n")
                        # * In second line storing name of the user
                        f.writelines(f"{userName}\n")
                        # * In third line storing Unique ID of the user
                        f.writelines(f"{self.UniqueID}")
                    # * After all these operations Seats are finaaly booked
                    print("Congratulations!!! Your seats are booked...")

            else:
                # * If more seats are asked to be booked then this statement will be fired
                print("Sorry! All seats are booked. Kindly try in tatkaal....")
        except Exception:
            # * This statement is fired when an error occured
            print('Error occured.. Please enter a number')

    def cancel_ticket(self):  # * This function is fired when user want to cancel booked tickets

        try:  # * Try statement is added in case program throws an error so that it will not crash
            # * It will ask the unique ID of the user provided at the time of booking of tickets
            uniqueID = int(input("Enter your Unique ID: "))
            # * Then If unique ID will match the file in Unique ID's Folder program will continue
            with open(f"Unique ID's/{uniqueID}.txt") as f:
                read = f.readline()  # * Reading first line of that unique ID file
                print("Gathering Information............")
                time.sleep(1.5)
                print(f"Seats Booked: {read}")
                read1 = f.readline()  # * Reading second line of that unique ID file
                print(f"Name of receipant: {read1}")
                read2 = f.readline()  # * Reading third line of that unique ID file
                print(f"Your unique ID: {read2}")
                time.sleep(1.7)

                if (int(read) == 1):  # * This if block statement is executed if user have booked only one seat
                    #! Printing and asking Captach from user
                    print(f"Captcha - {self.captcha}")
                    cap = input(
                        "Enter the Captcha or press O to exit the portal: ")
                    #! If entered captcha is right then this block is executed
                    # * Asking username to continue the program
                    user_name = input("Enter your name as shown above: ")
                    if (cap == self.captcha):
                        # * It will add 1 seat in Train.seats as 1 seat is cancelled
                        Train.seats = Train.seats + 1
                        remainSeats = 0  # * Now seat remaining is zero
                        # * Updating seats in avilableSeats.txt in write mode
                        with open('Train Info/availableSeats.txt', 'w') as f:
                            f.write(str(Train.seats))
                        # * Updating Info like name seats and unique ID in Uniwe ID's/User Unique ID file.txt
                        with open(f"Unique ID's/{uniqueID}.txt", 'w') as f:
                            f.write(f"{remainSeats}\n")
                            f.writelines(read1)
                            f.writelines(read2)
                        #! Making changes in the receipt of user and overwriting the changes in it
                        with open(f"Booked Tickets/{user_name}.txt", 'w') as f:
                            bookTicketReceipt2 = (f'''\t******************************* YOUR SEATS ARE Cancelled *******************************
NAME OF THE TRAIN IS: {self.TrainName}
NAME OF RECEIPANT: {read1}
SEATS BOOKED: 0
DESTINATION: {self.Destination}
AMOUNT TO PAY: 0 Rs.
RECEIPT GENERATED ON: {self.date}
TIME OF BOOKING: {self.current_time}
YOUR UNIQUE ID: {self.UniqueID}


************************ THANKS FOR USING OUR SERVICE. HAVE A GOOD DAY {user_name}************************''')
                            f.write(bookTicketReceipt2)
                    elif (cap == 'O'):  # * IF O is enteredin captcha the program will be exited
                        print("Exiting frome the portal...")
                        time.sleep(0.5)
                        exit()
                    else:
                        # * If enterd captcha is wrong then this command will be fired
                        print("Invalid Captcha")
                # * This if block statement is executed if user have booked more than one seat
                elif (int(read) > 1):
                    ask_seat = int(
                        input("Enter the number of seats you want to cancel: "))  # * Asking user to enter the number of seats he wnats to cancel
                    if (ask_seat <= int(read)):
                        # * Asking username to continue the program
                        new_name = input("Enter your name as shown above: ")
                        print(f"Captcha - {self.captcha}")
                        time.sleep(1)
                        # * If 0 is pressed then program will be exited
                        cap = input("Enter the Captcha or Press O to exit: ")
                        #! If entered captcha is right then this block is executed
                        if (cap == self.captcha):
                            time.sleep(1.5)
                            # * It will add all the seats cancelled by the user.
                            Train.seats = Train.seats + ask_seat
                            # * Updating seats in avilableSeats.txt in write mode
                            with open('Train Info/availableSeats.txt', 'w') as f:
                                f.write(str(Train.seats))
                            print(
                                f"{ask_seat} Seats are successfully cancelled")
                            f.close()
                            #! Updating Info like name seats and unique ID in Uniwe ID's/User Unique ID file.txt
                            with open(f"Unique ID's/{uniqueID}.txt", 'r') as f:
                                first_line = f.readline()
                            new_seats = str(int(first_line)-int(ask_seat))
                            with open(f"Unique ID's/{uniqueID}.txt", 'w') as f:
                                f.write(f"{new_seats}\n")
                                f.writelines(read1)
                                f.writelines(read2)
                            #! Making changes in the receipt of user and overwriting the changes in it
                            with open(f"Booked Tickets/{new_name}.txt", 'w') as f:
                                bookTicketReceipt = (f'''\t******************************* YOUR SEATS ARE BOOKED *******************************
NAME OF THE TRAIN IS: {self.TrainName}
NAME OF RECEIPANT: {read1}
SEATS BOOKED: {new_seats}
DESTINATION: {self.Destination}
AMOUNT TO PAY: {int(new_seats)*self.Fare} Rs.
RECEIPT GENERATED ON: {self.date}
TIME OF BOOKING: {self.current_time}
YOUR UNIQUE ID: {self.UniqueID}


    USE YOUR UNIQUE ID AT PAYMENT AND TO GET PHYSICAL TICKETS.....


************************ THANKS FOR USING OUR SERVICE. HAVE A GOOD DAY {new_name}************************''')
                                f.write(bookTicketReceipt)
                        elif (cap == 'O'):  # * IF O is enteredin captcha the program will be exited
                            print("Exiting frome the portal...")
                            time.sleep(0.5)
                            exit()
                        else:
                            # * If enterd captcha is wrong then this command will be fired
                            print("Invalid Captcha..........")
                    else:  # * By mistake if user appeals to cancel seats more than he booked then else block will be executed
                        print(
                            f"You have booked only {int(read)} seats")
                        time.sleep(1.7)
                # * If all seats are cancelled and still user appeals to cancel seats then this block is executed
                elif (int(read) == 0):
                    print("All seats are already cancelled!!")
                    time.sleep(2)
        except Exception:
            print("An unknown Error occured or ID not existed")

    @staticmethod
    def welcomeMsg():  # * This function is creted to display opening message to user when he enters in the program
        print('''\t******************************* WELCOME TO GUPTA EXPRESS ONLINE RESERVATION PORTAL *******************************
1) GET TRAIN INFROMATION                                                                                  2) BOOK TICKETS
3) CANCEL TICKETS                                                                                         4) EXIT PORTAL''')

    @staticmethod
    def progressBar():  # * This function will display a progress bar, it is made for user experience call this function to use it
        for i in tqdm(range(101),
                      desc="Loading…",
                      ascii=False, ncols=75):
            time.sleep(0.01)


if __name__ == "__main__":  # * This statement will not allow to access it's code to other python .py files
    while True:  # * Infnite Loop so that program not ends until the exit command is not given
        Numbers = "1234567890"
        length = 6
        new_length = 5
        # * New unique Id is generated every time and stored in this variable
        unique = "".join(random.sample(Numbers, length))
        words = "ABCDEFGHIJKLMNOP"
        new_all = words+Numbers
        # * New captcha is generated every time and stored in this variable
        new_captcha = "".join(random.sample(new_all, new_length))
        # * Our raliway code is 5510 which is included in the begining of every unique ID
        ID = "5510"+unique
        # * Passing variable and string in constructor
        guptaExpress = Train(ID, "DELHI TO PUNE", new_captcha)
        guptaExpress.welcomeMsg()  # * Display a welcome Message when the program begins
        # * All the time.sleep() function is added to take a break and then execute the next line
        time.sleep(1.5)
        try:  # * Try statement is added in case program throws an error so that it will not crash
            # * Asking user to enter the desired command  whether 1,2,3,4
            select = int(input("Enter your Choice\n"))
            if (select == 1):  # * If 1 is given the train_info() function will be executed
                guptaExpress.progressBar()
                print("FETCHING TRAIN INFO.......")
                time.sleep(1.5)
                guptaExpress.train_info()
                time.sleep(2)
            elif (select == 2):  # * If 2 is given the Book_ticket() function will be executed
                guptaExpress.progressBar()
                print(
                    "************************* WELCOME TO BOOK TICKETS PORTAL *************************")
                time.sleep(1.5)
                guptaExpress.Book_ticket()
                time.sleep(2)
            elif (select == 3):  # * If 3 is given the cancel_ticket() function will be executed
                guptaExpress.progressBar()
                print(
                    "\t**************************** WELCOME TO OUR SEATS CANCELLATION PORTAL **************************** ")
                time.sleep(0.5)
                print("Please Wait for a while ..........................")
                time.sleep(1.5)
                guptaExpress.cancel_ticket()
                time.sleep(2)
            elif (select == 4):  # * If 4 is given the program will be closed with a closing message
                print("\t#############################################  Thanks for using our portal  #############################################")
                time.sleep(3)
                exit()
            else:
                print("Enter a valid number!!!!!")
                time.sleep(2)
        except Exception:
            # * This statement is fired when an error occured
            print("Enter the options in number only!!")
            time.sleep(1.2)
