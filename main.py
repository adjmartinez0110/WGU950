#Student ID: 001519423
#This is the main Python program.
import hash_table
import truck
from package import *
from truck import *
import datetime
import csv

#Creating and loading the trucks
truck1 = Truck(1,16, [1,2,4,5,7,8,13,14,15,16,18,19,20,30,31], "4001 South 700 East", datetime.timedelta(hours=8),0)
truck2 = Truck(2,16, [3,6,10,11,12,17,21,22,23,24,26,27,29,36,38], "4001 South 700 East", datetime.timedelta(hours=9, minutes=10),0)
truck3 = Truck(3,16, [9,25,28,32,33,34,35,37,39,40], "4001 South 700 East", datetime.timedelta(hours=11),0)



#Reading in the name of addresses from csv file (addresses)
with open('Names of distances v2.csv') as addresscsv:
    read_address = csv.reader(addresscsv, delimiter=',')
    read_address = list(read_address)

#Reading in the name of address from the csv file (distances) and place them into a list
with open('Numerical distances.csv') as distancecsv:
    read_distance = csv.reader(distancecsv, delimiter=',')
    read_distance = list(read_distance)



#Address lookup function -> Big O of: O(N)
def address_lookup(address):
    count = 0
    for i in read_address:
        if address == i[0]:
            return count
        else:
            count = count + 1

#Getting the current distance -> Big O of O(1)
def current_distance(row, column):
    distance = read_distance[row][column]
    if distance == '':  # if distance empty
        distance = read_distance[column][row]

    return float(distance)

#Determining delivery status of package -> Big O of O(1)
def confirm_delivery(package, user_time):
    if package.packID == 9:
        if user_time < datetime.timedelta(hours=10, minutes=20):
            package.address = "300 State St"
        else:
            package.address = "410 S State St"

    if user_time < package.time_lefthub:
        package.status = "At Hub"
        package.display_delivery_time = " "
    elif user_time >= package.time_lefthub and user_time < package.time_delivered:
        package.status = "In Route"
        package.display_delivery_time = " "
    else:
        package.status = "Delivered"
        package.display_delivery_time = package.time_delivered


#Implementation of the nearest neighbor algorithm Big O -> O(N^2)
#The algorithm contains a nested loop. A while loop determines that as
#the truck still has packages to deliver, the truck continues on its route.
#The for loop within determines which package to deliver next based on truck's
#current location. This nested loop structure contributes to the function's
#Big O structure.
def nearest_neighbor(truck):

    total_distance = 0
    current_time = truck.depart_time

    for i in truck.packages:
        package = myHash.search(i)
        package.time_lefthub = truck.depart_time

    while truck.packages:

        min_distance = 255
        min_packageID = None


        for packageID in truck.packages:
            package = myHash.search(packageID)

            #find truck's current location
            truck_coords = address_lookup(truck.address)

            #find destination of next nearest package
            package_coords = address_lookup(package.address)

            #find the distance between the two previous locations
            distance = current_distance(truck_coords, package_coords)


            if distance < min_distance:
                #this new distance becomes the next location for truck to visit
                min_distance = distance

                #mark the package that is the next one to be delivered
                min_packageID = package.packID

        # Move the truck to the location of the nearest package and mark timestamp
        package_to_deliver = myHash.search(min_packageID)
        truck.address = package_to_deliver.address
        current_time = current_time + datetime.timedelta(hours=min_distance/18)

        # Mark package as delivered and mark truck it was delivered from
        package_to_deliver.time_delivered = current_time
        package_to_deliver.truck_number = truck.id

        # Remove package from truck once delivered
        truck.packages.remove(min_packageID)

        # Update total distance after delivering the current package
        total_distance = total_distance + min_distance

    # Calculate and add the distance to return to the starting location
    return_to_hub = current_distance(0, address_lookup(truck.address))
    total_distance = total_distance + return_to_hub
    truck.mileage = total_distance


# Calling nearest neighbor
nearest_neighbor(truck1)
nearest_neighbor(truck2)
nearest_neighbor(truck3)

#Main program start
print("Welcome to the Western Governors University (WGUPS) Routing Program")
print("*******************************************************************")
print("                                                                   ")

print("Total mileage for all trucks is " + str(truck1.mileage + truck2.mileage + truck3.mileage) + " miles.")
print(" ")


#Formatting entered time to timedelta object
prompt_time = input("To view the status of a package at a specific time, enter time in HH:MM format: ")
(hour, minute) = prompt_time.split(":")
formatTime = datetime.timedelta(hours=int(hour), minutes=int(minute))
print(" ")

#Asking the user if they want to view all packages or a single one
answer = int(input("Would you like to view all package info at a particular time or a single package? Press 1 for All or 2 for single package: "))
print(" ")

if answer == 1:
   for packageID in range(1,41):
       package = myHash.search(packageID)
       confirm_delivery(package, formatTime)
       print(package)

elif answer == 2:
    package_to_view = int(input("Please enter a package number from 1 to 40 to view details on a package: "))

    if package_to_view < 1 or package_to_view > 40:
        print("Package number not found. Please try again.")
    else:
        for packageID in range(1,41):
            if packageID == package_to_view:
                package = myHash.search(package_to_view)
                confirm_delivery(package, formatTime)
                print(package)

else:
    print("Unknown error occurred")
