#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from car import Car

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
    # Now addign some more details about the battery as we want without cluttering the ElectricCar class.    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print("This car can go approximately " + str(range) + " miles on a full charge.") 


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

