
#The four Pillars.
# Inheritance = a way to pass on attributes and methods defined in a parent class,
# so that they can also be accessed from a child class
# Inheritance can be implemented by mentioning the name of the parent class in round brackets
# a child class can inherit any parent class

# Abstraction = a way we can force classes that inherit an abstract class to define a certain behavior
# there are two methods of abstraction:
# a) all methods in a class are abstract - the class will be called an interface
# b) only some of the methods in a class are abstract - the class will be called an abstract class
# If we define a child class that samples an abstract class / interface and we don't implement the abstract methods,
# then we will get an error


# Polymorphism = a way in which we can implement multiple functions with the same name but different behavior
# there are several ways to implement polymorphism:
# a) polymorphism by implementing the same method in two different classes
# b) polymorphism by reimplementing the method in the parent class
# c) polymorphism by defining a function or method with implicit parameters
# d) polymorphism by defining a function or method with *args


# encapsulation = a way to restrict access to certain attributes or methods
# there are three types of access:
# public = we can access the attributes and methods of the class anywhere in the program
# private = we can access attributes and methods of the class only inside the class (self)
# protected = we can only have access to attributes and methods of the class in the same package as the class


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


#Competition-Inheritance

class Sports_competitions():
    competition_type = None
    age_category = None
    number_participants = None
    distance = None
    dificulty = None
    awards = {}
    official_sponsor = None

    def __init__(self, competition_type,location,distance):
        self.competition_type = competition_type
        self.location = location
        self.distance = distance

    def premiere_participanti(self,first,second,third):
        self.awards["first_place"] = first
        self.awards["second_place"] = second
        self.awards["third_place"] = third

    def results(self):
        for key,values in self.awards.items():
            print(f"{key} : {values}")

class Marathon(Sports_competitions):
    preparation = None
    location = None
    num_checkpoint = None

    def checkpoint(self):
        if self.num_checkpoint <4:
            self.num_checkpoint+=1

marathon = Marathon("marathon","county","42")
marathon.pregatire_competitie = "running plan"
marathon.premiere_participanti("Ionut Florescu","Ramona Vascul","Catalin Stefan")
marathon.results()