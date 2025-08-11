class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start(self):
        return f"The {self.make} {self.model} is starting"
    
    def stop(self):
        return f"The {self.make} {self.model} is stopping"
    
    def get_info(self):
        return f"Vehicle: {self.make} {self.model}"

class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    
    # Override the start method
    def start(self):
        return f"The electric {self.make} {self.model} is silently starting"
    
    # Override the get_info method
    def get_info(self):
        parent_info = super().get_info()  # Call parent method
        return f"{parent_info}, Battery: {self.battery_capacity}kWh"
    
    # New method
    def charge(self):
        return f"Charging the {self.make} {self.model}"

# Create objects
regular_car = Vehicle("Toyota", "Camry")
electric_car = ElectricCar("Tesla", "Model 3", 75)

# Compare method calls
print(regular_car.start())      # The Toyota Camry is starting
print(electric_car.start())     # The electric Tesla Model 3 is silently starting

print(regular_car.get_info())   # Vehicle: Toyota Camry
print(electric_car.get_info())  # Vehicle: Tesla Model 3, Battery: 75kWh

print(electric_car.charge())    # Charging the Tesla Model 3