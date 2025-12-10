# Simple Inheritance 

class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
class Cat(Animal):
    def speak(self):
        return "Cat meows"
    
print()
dog = Dog()
cat = Cat()
print(dog.speak())  
print(cat.speak())  

# Multi-level Inheritance

class Vehicle:
    def start(self):
        return "Vehicle started"
class Car(Vehicle):
    def drive(self):
        return "Car is driving"
class SportsCar(Car):
    def turbo_boost(self):
        return "SportsCar turbo boost activated"

print()
sports_car = SportsCar()
print(sports_car.start())
car = Car()
print(car.drive())

# Hierarchical Inheritance

class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    
print()
rectangle = Rectangle(4, 5)
circle = Circle(3)
print(f"Rectangle Area: {rectangle.area()}")
print(f"Circle Area: {circle.area()}")

# Multiple Inheritance

class Flyer:
    def fly(self):
        return "Flying"
    def name(self):
        return "Flyer"
class Swimmer:
    def swim(self):
        return "Swimming"
    def name(self):
        return "Swimmer"
class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack Quack"
    
print()
duck = Duck()
print(duck.fly())
print(duck.swim())
print(duck.quack())
print(duck.name())

# Hybrid Inheritance

class LivingBeing:
    def breathe(self):
        return "Breathing"
class Mammal(LivingBeing):
    def walk(self):
        return "Walking"
class Whale(Mammal):
    def swim(self):
        return "Swimming"
    
print()
whale = Whale()
print(whale.breathe())
print(whale.walk())
print(whale.swim())