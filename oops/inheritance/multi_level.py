# A --> B-->--C
# Grandparent Class
class Vehicle:
    def start(self):
        print("Engine started.")

# Parent Class (Inherits from Vehicle)
class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

# Child Class (Inherits from Car)
class ElectricCar(Car):
    def charge(self):
        print("Battery is charging.")

# --- Demonstration ---
my_ev = ElectricCar()

# ElectricCar accesses methods from ALL levels above it
my_ev.start()   # From Vehicle (Grandparent)
my_ev.drive()   # From Car (Parent)
my_ev.charge()  # From ElectricCar (Itself)
