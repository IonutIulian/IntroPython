

# HOMEWORK 7 - The Four pillars of OOPs Object Oriented Programming

# ABSTRACTION
# Abstract class GeometricShape
# Contains a field PI=3.14
# Contains an abstract method aria (optional)
# Contains a method of class describe() - this prints 'Most
# probably have corners'
# INHERITANCE
# Class Square - inherits GeometricShape
# constructor for the side
#
# ENCAPSULATION
# side is private property
# Implements getter, setter, deleter for side
# Implements the method required by the interface (optional, only if you chose to
# implement the abstract aria method)
# Circle class - inherits GeometricShape
# constructor for radius
# radius is private property
# Implements getter, setter, deleter for radius
# Implements the method required by the interface - in calculation uses field PI
# inherited from the parent class (optional, only if you chose to implement the
# abstract aria method)
# POLYMORPHISM
# Defines a new describe method - prints 'I have no corners'
# Create a square object and play with its methods
# Create a Circle object and play with its methods

from abc import  ABC, abstractmethod
import math
class GeometricForm(ABC):
    PI = 3.14

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("Probably i have nooks.")


class Square(GeometricForm):

    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def get_side(self):
        return self.side

    def del_side(self):
        del self.side
        print("The side of the square has been deleted")

    def area(self):
        return self.side **2

    def perimetre(self):
        return self.side*4

    def diagonal(self):
        return self.side * math.sqrt(2)

class Circle(GeometricForm):

        def __init__(self, radius):
            self.radius = radius

        def set_radius(self, radius):
            self.radius = radius

        def get_radius(self):
            return self.radius

        def del_radius(self):
            del self.radius
            print("The redius of the circle has been deleted.")

        def area(self):
            return  self.PI * (self.radius ** 2)

        def diametre(self):
            return self.radius *2

        def circumference(self):
            return self.PI *2 *self.radius



geo1 = Square(4)
geo2 = Circle(6)
geo1.describe()
geo2.describe()
print(f"The side of the square {geo1.get_side()} cm, so the square has an area of  "
      f" {geo1.area()} square cm .The perimetre of the square is {geo1.perimetre()} cm  and the diagonal is"
      f" {geo1.diagonal()} cm")

print(f"The radius of the circle has {geo2.get_radius()} cm and the diametre {geo2.diametre()} cm."
      f"The area of the circle has   {geo2.area()} square cm, and the circumference {geo2.circumference()} cm.")


geo1.del_side()
geo2.del_radius()


sid = float(input("Enter value for the side of the square: "))
rad = float(input("Enter value for the radius of the circle: "))
geo3= Square(sid)
geo4 = Circle(rad)

print(f"The side of the square {geo3.get_side()} cm, so the square has an area of  "
      f" {geo3.area()} square cm .The perimetre of the square is {geo3.perimetre()} cm  and the diagonal is"
      f" {geo3.diagonal()} cm")

print(f"The radius of the circle has {geo4.get_radius()} cm and the diametre {geo4.diametre()} cm."
      f"The area of the circle has   {geo4.area()} square cm, and the circumference {geo4.circumference()} cm.")

geo3.del_side()
geo4.del_radius()