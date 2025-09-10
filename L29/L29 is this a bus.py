class vehicle: # parent class
    def __init__(self, nm, speed, mile):
        self.name = nm
        self.max_speed = speed
        self.mileage = mile

class Bus(vehicle): #child class
    pass

#object creation
School_bus = Bus("School Ford", 100, 10)

print(f"Vehicle Name: {School_bus.name}")
print(f"Speed: {School_bus.max_speed}")
print(f"Mileage: {School_bus.mileage}")