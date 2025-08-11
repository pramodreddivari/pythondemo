class Flyable:
    def fly(self):
        return "Flying through the air"
    
    def land(self):
        return "Landing safely"

class Swimmable:
    def swim(self):
        return "Swimming in water"
    
    def dive(self):
        return "Diving underwater"

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# Multiple inheritance
class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name)
    
    def quack(self):
        return f"{self.name} says Quack!"

class Fish(Animal, Swimmable):
    def __init__(self, name):
        super().__init__(name)

class Bird(Animal, Flyable):
    def __init__(self, name):
        super().__init__(name)

# Create objects
duck = Duck("Donald")
fish = Fish("Nemo")
bird = Bird("Eagle")

# Duck has methods from all parent classes
print(duck.eat())       # Donald is eating
print(duck.fly())       # Flying through the air
print(duck.swim())      # Swimming in water
print(duck.quack())     # Donald says Quack!

# Fish has methods from Animal and Swimmable
print(fish.swim())      # Swimming in water
print(fish.dive())      # Diving underwater

# Bird has methods from Animal and Flyable
print(bird.fly())       # Flying through the air
print(bird.land())      # Landing safely

# Check inheritance
print(isinstance(duck, Animal))     # True
print(isinstance(duck, Flyable))    # True
print(isinstance(duck, Swimmable))  # True
print(isinstance(fish, Flyable))    # False