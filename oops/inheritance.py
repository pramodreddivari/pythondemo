# Parent class (Base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    
    def make_sound(self):
        return f"{self.name} makes a sound"
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent constructor
        self.breed = breed
    
    def make_sound(self):  # Override parent method
        return f"{self.name} barks: Woof!"
    
    def fetch(self):  # New method specific to Dog
        return f"{self.name} fetches the ball"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):  # Override parent method
        return f"{self.name} meows: Meow!"
    
    def climb(self):  # New method specific to Cat
        return f"{self.name} climbs the tree"
    
# Create objects
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

# Use inherited methods
print(dog.eat())        # Buddy is eating
print(cat.sleep())      # Whiskers is sleeping

# Use overridden methods
print(dog.make_sound()) # Buddy barks: Woof!
print(cat.make_sound()) # Whiskers meows: Meow!

# Use specific methods
print(dog.fetch())      # Buddy fetches the ball
print(cat.climb())      # Whiskers climbs the tree

# Access attributes
print(f"{dog.name} is a {dog.breed} {dog.species}")
print(f"{cat.name} is a {cat.color} {cat.species}")        
        