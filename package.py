#This package program will hold info on packages with 8 fields includes in the Excel file; this takes the hard coded
#approach to package data
import datetime

from hash_table import myHash

class Package:

    # initialize method Big O -> O(1)
    def __init__(self, packID, address, city, state, zip, deadline, weight, notes):
        self.packID = packID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.time_delivered = None
        self.time_lefthub = None
        self.status = "At Hub"
        self.truck_number = 0
        self.display_delivery_time = " "

    def __str__(self):  # Overwriting print(package)  Big O -> O(1)
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, Truck:%s" % (
            self.packID, self.address, self.city, self.state, self.zip,  self.weight, self.notes, self.time_lefthub, self.deadline, self.display_delivery_time,  self.status, self.truck_number)


#package objects
package1 = Package(1,"195 W Oakland Ave", "Salt Lake City", "UT", 84115, "10:30 AM", 21, "None")
package2 = Package(2,"2530 S 500 E","Salt Lake City","UT", 84106, "EOD", 44, "None")
package3 = Package(3,"233 Canyon Rd","Salt Lake City","UT", 84103, "EOD", 2, "Can only be on truck 2")
package4 = Package(4,"380 W 2880 S","Salt Lake City","UT", 84115, "EOD", 4, "None")
package5 = Package(5,"410 S State St","Salt Lake City","UT", 84111, "EOD", 5, "None")
package6 = Package(6,"3060 Lester St","West Valley City","UT", 84119, "10:30 AM", 88, "Delayed on flight - will not arrive to depot until 9:05 AM")
package7 = Package(7,"1330 2100 S","Salt Lake City","UT", 84106, "EOD", 8, "None")
package8 = Package(8,"300 State St","Salt Lake City","UT", 84103, "EOD", 9, "None")
package9 = Package(9,"410 S State St","Salt Lake City","UT", 84111, "EOD", 2, "Address corrected at 10:20")
package10 = Package(10,"600 E 900 S","Salt Lake City","UT", 84105, "EOD", 1, "None")
package11 = Package(11,"2600 Taylorsville Blvd","Salt Lake City","UT", 84118, "EOD", 1, "None")
package12 = Package(12,"3575 W Valley Central Station bus Loop","West Valley City","UT", 84119, "EOD", 1, "None")
package13 = Package(13,"2010 W 500 S","Salt Lake City","UT", 84104, "10:30 AM", 2, "None")
package14 = Package(14,"4300 S 1300 E","Millcreek","UT", 84117, "10:30 AM", 88, "Must be delivered with 15, 19")
package15 = Package(15,"4580 S 2300 E", "Holladay", "UT", 84117, "09:00 AM", 4, "None")
package16 = Package(16,"4580 S 2300 E","Holladay","UT", 84117, "EOD", 88, "Must be delivered with 13, 19")
package17 = Package(17,"233 Canyon Rd","Salt Lake City","UT", 84119, "EOD", 2, "None")
package18 = Package(18,"1488 4800 S","Salt Lake City","UT", 84123, "EOD", 6, "Can only be on truck 2")
package19 = Package(19,"177 W Price Ave","Salt Lake City","UT", 84115, "EOD", 37, "None")
package20 = Package(20,"3595 Main St","Salt Lake City","UT", 84115, "10:30 AM", 37, "Must be delivered with 13, 15")
package21 = Package(21,"3595 Main St","Salt Lake City","UT",84115,"EOD",3, "None")
package22 = Package(22,"6351 S 900 E","Murray","UT",84121, "EOD",2,"None")
package23 = Package(23,"5100 S 2700 W","Salt Lake City","UT",84118,"EOD",5,"None")
package24 = Package(24,"5025 State St","Murray","UT",84107,"EOD",7,"None")
package25 = Package(25,"5383 S 900 E #104","Salt Lake City","UT",84117,"10:30 AM",7,"Delayed on flight---will not arrive to depot until 9:05 AM")
package26 = Package(26,"5383 S 900 E #104","Salt Lake City","UT",84117,"EOD",25,"None")
package27 = Package(27,"1060 Dalton Ave S","Salt Lake City","UT",84104,"EOD",5, "None")
package28 = Package(28,"2835 Main St","Salt Lake City","UT",84115,"EOD",7,"Delayed on flight---will not arrive to depot until 9:05 AM")
package29 = Package(29,"1330 2100 S","Salt Lake City","UT",84106,"10:30 AM",2,"None")
package30 = Package(30,"300 State St","Salt Lake City","UT",84103,"10:30 AM",1,"None")
package31 = Package(31,"3365 S 900 W","Salt Lake City","UT",84119,"10:30 AM",1,"None")
package32 = Package(32,"3365 S 900 W","Salt Lake City","UT",84119,"EOD",1,"Delayed on flight---will not arrive to depot until 9:05 AM")
package33 = Package(33,"2530 S 500 E","Salt Lake City","UT",84106,"EOD",1,"None")
package34 = Package(34,"4580 S 2300 E","Holladay","UT",84117,"10:30 AM",2,"None")
package35 = Package(35,"1060 Dalton Ave S","Salt Lake City","UT",84104,"EOD",88,"None")
package36 = Package(36,"2300 Parkway Blvd","West Valley City","UT",84119,"EOD",88,"Can only be on truck 2")
package37 = Package(37,"410 S State St","Salt Lake City","UT",84111,"10:30 AM",2,"None")
package38 = Package(38,"410 S State St","Salt Lake City","UT",84111,"EOD",9,"Can only be on truck 2")
package39 = Package(39,"2010 W 500 S","Salt Lake City","UT",84104,"EOD",9,"None")
package40 = Package(40,"380 W 2880 S","Salt Lake City","UT",84115,"10:30 AM",45,"None")

#list to hold the objects
package_list = [package1, package2, package3, package4, package5, package6, package7, package8, package9, package10,
                package11, package12, package13, package14, package15, package16, package17, package18, package19, package20,
                package21, package22, package23, package24, package25, package26, package27, package28, package29, package30,
                package31, package32, package33, package34, package35, package36, package37, package38, package39, package40]

# Will use a for loop to insert package data into hash table using the list of packages
for package in package_list:
    myHash.insert(package.packID, package)




