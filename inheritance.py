# :

# 🔧 Challenge: Inheritance and Method Overriding
# Create a base class called Vehicle with the following:

# An __init__ method that sets the brand and model.

# A method start_engine() that prints "Engine started".

# Then, create a subclass called ElectricVehicle that:

# Inherits from Vehicle.

# Adds a new attribute battery_capacity.

# Overrides the start_engine() method to print "Electric engine started silently".

# ✍️ Your Task
# Write the full class definitions for Vehicle and ElectricVehicle.

# Create an instance of ElectricVehicle and call start_engine() on it.

# Print the brand, model, and battery_capacity of the instance.
# "<brand> <model> with <battery_capacity> battery"

# 🔧 Challenge: Encapsulation with Getters and Setters
# Update your ElectricVehicle class to:

# Add a protected attribute _battery_health set to 100.

# Add a private attribute __internal_id set to "EV0001".

# Add a method get_internal_id() to safely access __internal_id.

# Add a method degrade_battery(amount) that reduces _battery_health by amount.


# 🔧 Quick Challenge: Apply Both in Your Class
# In your ElectricVehicle class:

# Add a class attribute vehicle_counter initialized to 0.

# Add a @classmethod called increment_vehicle_count() that updates this counter.

# Add a @staticmethod called convert_kwh_to_mwh(kwh) that converts battery capacity.

# Then test:

# python
# Copy
# Edit
# ElectricVehicle.increment_vehicle_count()
# print(ElectricVehicle.vehicle_counter)

# print(ElectricVehicle.convert_kwh_to_mwh(400))  # Should return 0.4




class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return "Engine started"
class ElectricVehicle(Vehicle):
    vehicle_counter = 0
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        self._battery_health= 100
        self.__internal_id = "EV0001"
    
    @classmethod
    def increament_vehicle_count(cls):
        cls.vehicle_counter += 1
        return cls.vehicle_counter

    def convert_kwh_to_mwh(self,amount):
        self.battery_capacity /= 1000
        return self.battery_capacity
        
    
        
    def get_internal_id(self):
        return self.__internal_id
    
    def degrade_battery(self,amount):
        self._battery_health -= amount
        return self._battery_health
        
    def __str__(self):
        return f"{self.brand}  {self.model} with {self.battery_capacity} battery"
    def start_engine(self):
        super().start_engine()
        return  "Electric engine started silently"
    
    
obj = ElectricVehicle("Mazda", "Toyota", 40)
# print(obj)
# print(obj._battery_health)          # (Should work but discouraged)
# print(obj.get_internal_id())        # (Proper way to get internal ID)
# obj.degrade_battery(10)
# print(obj._battery_health)          # Should now be 90
print(obj.increament_vehicle_count())
print(obj.vehicle_counter)
print(obj.convert_kwh_to_mwh(50))
# print(f"{[obj.brand, obj.model, obj.battery_capacity]}")