#Truck class

class Truck:

 #Big O -> O(1)
 def __init__(self, id, capacity, packages, address, depart_time, mileage):
    self.id = id
    self.capacity = capacity
    self.packages = packages
    self.address = address
    self.depart_time = depart_time
    self.mileage = mileage

 #Big O -> O(1)
 def __str__(self):
     return "%s, %s, %s, %s, %s, %s" % (self.id, self.capacity, self.packages, self.address, self.depart_time, self.mileage)