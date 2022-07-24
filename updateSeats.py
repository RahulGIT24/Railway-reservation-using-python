
#* THIS PROGRAM IS CREATED FOR RAILWAY OFFICIALS  THROUGH THIS THEY CAN UPDATE THE TRAIN SEATS AND FARE PRICE...

#! Modules used
import main
import time


print('\t***********************************************************************')

print(f'Currently seats available in Train are: {main.Train.seats}')
print(f'Currently train fare is {main.Train.Fare}')

print('\t***********************************************************************')
while True:

    print('''\t ******************* What do you want to update?? ******************* 
1) SEATS
2) FARE 
3) EXIT''')

    ask = int(input('Enter any one of them: '))

    try:
        if (ask == 1):
            addSeats = int(input("Enter the seats you want to add:  "))
            with open('Train Info/availableSeats.txt', 'r') as f:
                readFile = f.read()
            print('Loading..................')
            time.sleep(2)
            print('Seats Updated')
            with open('Train Info/availableSeats.txt', 'w') as f:
                updatedSeats = (int(readFile)+int(addSeats))
                f.write(str(updatedSeats))
        elif (ask == 2):
            newFare = int(input("Enter the new Fare amount: "))
            print('Loading..................')
            time.sleep(2)
            print('Fare Updated')
            with open('Train Info/fare.txt', 'w') as f:
                f.write(str(newFare))
        elif (ask == 3):
            print("Theek hai ab mai chalta hun...")
            time.sleep(2)
            exit()
        else:
            print("Enter a valid choice")
    except Exception:
        print("Error Occured!!!!!!!!!!!")
