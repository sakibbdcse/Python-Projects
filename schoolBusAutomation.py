class Vehicle:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

class Bus(Vehicle):
    pass  

school_bus = Bus(70, 20)

print(school_bus.max_speed, school_bus.milage)
