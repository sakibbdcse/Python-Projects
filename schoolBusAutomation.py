class Vehicle:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

    def sitting_capacity(self, capacity):
        return f"Sitting capacity of the vehicle is {capacity} passengers."

class Bus(Vehicle):
    def sitting_capacity(self, capacity=50):
        return f"Sitting capacity of the bus is {capacity} passengers."

# Creating a Bus object
school_bus = Bus(70, 20)

# Displaying the sitting capacity and other attributes
print(school_bus.sitting_capacity())  # Default capacity is 50
print(school_bus.max_speed, school_bus.milage)
