# # Defining a class
# class Car:
#     color = "red"  # Attribute(characteristic)

#     # Method(behavior)
#     def drive(self):
#         print("The car is driving 🚗")

# # Creating an object
# my_car = Car()
# print(my_car.color)
# my_car.drive()

# Creating another object
# class Bed:
#     size = "queen"  # Attribute(properties)
#     color = "white"  
#     type = "mahogany"

#     # Method(behavior)
#     def sleep(self):
#         print("All night sleep 😴")
        
#         wakeup = Bed()
#         print(wakeup.size)
#         wakeup.sleep()

# self is just a reference to the current instance of the class like  a pointer 


# class Car:
#     def __init__(self, color, model):
#         self.color = color    # Instance variable
#         self.model = model    # Instance variable

# # Creating objects with unique attributes
# car1 = Car("blue", "Sedan")
# car2 = Car("red", "SUV")

# print(car1.model)  # Output: blue
# print(car2.model)  # Output: SUV

# INHERITANCE
# class Vehicle:
#     def __init__(self, wheels):
#         self.wheels = wheels

# class Car(Vehicle):
#     pass

# car = Car(4)
# print(car.wheels)  # Output: 4

# POLYMORPHISM
# class Dog:
#     def speak(self):
#         return "Woof!"

# class Cat:
#     def speak(self):
#         return "Meow!"

# # Polymorphism in action
# for animal in [Dog(), Cat()]:
#     print(animal.speak())

# ENCAPSULATION
# class SecretStash:
#     def __init__(self):
#         self.__chocolates = 10  # Private attribute

#     def take_chocolate(self):
#         if self.__chocolates > 0:
#             self.__chocolates = 1   # Decrease the number of chocolates
#             print("One chocolate taken!")
#         else:
#             print("No chocolates left 😢")

# stash = SecretStash()
# stash.take_chocolate()

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if new_radius >= 0:
            self._radius = new_radius
        else:
            raise ValueError("Radius cannot be negative.")

    radius = property(get_radius, set_radius)

    def area(self):
        return 3.14159 * (self.radius ** 2)  # Accessing via the property

c = Circle(5)
print(f"Radius: {c.radius}")
print(f"Area: {c.area()}")

c.radius = 7  # Using the setter
print(f"New radius: {c.radius}")

try:
    c.radius = -2
except ValueError as e:
    print(f"Error: {e}")