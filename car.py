#!/usr/bin/env python
# coding: utf-8

# In[ ]:


############# A class that can be used to represent a car. ##################

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.year = year
        self.model = model
        self.odometer_reading = 0
        
    def descriptive_name(self):
        print(str(self.year) + ' ' + self.make.title() + ' ' + self.model)
        
    def read_odometer(self):
        print("This car has" + ' ' + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self,milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cannot roll back odometer reading")
            
    # If we want to reject negative increments so no one uses this function to roll back an odometer        
    def increment_odometer(self,miles):
        if miles > 0 :
            self.odometer_reading += miles
            print("The updated odometer reading is " + str(self.odometer_reading) + ' ' + "miles." )
        else:
            print("You cannot roll back odometer reading")
            
    def fill_gas_tank(self):
        if self.odometer_reading <= 1000:
            print("No need to fill the tank as of now buddy")
        else:
            print("You need to fill your tank")

