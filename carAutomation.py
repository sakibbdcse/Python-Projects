class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        # Fuel capacity and level in gallons
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fuel_tank(self):
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full")

    def drive(self):
        print("Car is moving")

    def update_fuel_level(self,new_level):
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("The tank can't hold that much")
    
    def add_fuel(self,amount):
        if(self.fuel_level+amount <= self.fuel_capacity):
            print("added fuel")
        else:
            print("the tank can hold that much")

# Create an instance of Car
my_car = Car("Tesla", "G3", 2024)

# Set initial fuel level
my_car.fuel_level = 5

# Access attributes
print(my_car.make)           
print(my_car.model)          
print(my_car.year)           
print(my_car.fuel_capacity)  
print(my_car.fuel_level)     

# Call methods
my_car.fuel_tank()           
print(my_car.fuel_level)     
my_car.drive()
my_car.update_fuel_level(12)
my_car.fuel_level
my_car.add_fuel(4)