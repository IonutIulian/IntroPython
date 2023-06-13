

# HOMEWORK.6 - Object-oriented programming (OOP), Classes & Objects

# Class is a pattern/blueprint structure that serves as a guide to an item that might exist. It consists of :
# - attributes = the properties with which objects will be identified
# - methods = the actions an object can do
# The object is an instance of the class, the actual representation of the blueprint represented by the class,
# as many objects of a given class can be instantiated.

#1.1.Class Circle
# Attributes: radius, colour
# Constructor for both attributes
# Methods:
#  describe_circ() - will PRINT color and radius.
#  area() - will RETURN area
#  diameter()
#  circumference()

from math import pi

import self as self


class Circle:
    color = None,
    radius = None,

    def __init__(self,color,radius):
        self.color = color
        self.radius = radius

    def describe_circle(self):
        print(f"The circle is {self.color} color and radius {self.radius}.")

    def area(self):
        print(f"The area of the circle is {pi*(self.radius**2)} square metres.")

    def diameter(self):
        print(f'The diameter of the circle is  {self.radius*2} metres.')

    def circumference(self):
        print(f'The circumference of the circle is {pi*(2*self.radius)}.')
        print()



crc1 = Circle('white', 6)
crc2 = Circle('black', 7)
crc1.describe_circle()
crc1.area()
crc1.diameter()
crc1.circumference()
crc2.describe_circle()
crc2.area()
crc2.diameter()
crc2.circumference()

print()

#2.Rectangle Class
# Attributes: length, width, colour.Constructor for all attributes
# Methods:
#  describe()
#  area()
#  perimeter()
#  change_circle(new_circle) - this method returns nothing.
# It will take a new color as a parameter and override the self.color.

class Rectangle:
    length = None,
    width = None,
    color = None,

    def __init__(self, length, width , color):
        self.length = length
        self.width = width
        self.color = color

    def describe(self):
        print(f"The rectangle has the length equal with  {self.length} and thw width equal with {self.width}"
              f" and color: {self.color}.")

    def area(self):
        print(f"The area of the rectangle is  {self.width*self.length} square metres.")

    def perimeter(self):
        print(f"The perimeter is  {2*self.length+2*self.width} metres.")

    def change_color(self, new_color):
        self.color = new_color
        print(f"The new color is  {self.color}")
        print()

rec1 = Rectangle(6,4, "green")
rec2 = Rectangle(7,5, "silver")
rec2.describe()
rec2.area()
rec2.perimeter()
rec2.change_color("red")
rec1.describe()
rec1.area()
rec1.perimeter()
rec1.change_color("yelow")

print()

#3.Class Employee
# Attributes: first name, last name, salary.Constructor for all attributes
# Methods: describe()  full_name()  salary_monthly()  annual_wage()  salary_increase(percentage)

class Employee:
    firstname = None,
    lastname = None,
    wage = None,
    def __init__(self, lastname ,firstname , wage):
        self.lastname = lastname
        self.firstname = firstname
        self.wage = wage

    def describe(self):
        print(f"The employee  { self.firstname}  {self.lastname} has a wage of {self.wage} ron")

    def complet_name(self, father_initial):
        print(f"Numele complet al angajatului este { self.lastname}  {father_initial}  {self.firstname}")

    def monthly_wage(self):
        print(f"The monthly wage of the employee {self.lastname} is {self.wage} ron.")

    def anual_wage(self):
        print(f"The anual wage of the employee {self.lastname} is {self.wage*12} ron.")

    def increased_wage(self ,percentage):
        increased_value  = (self.wage * (percentage/100))
        self.wage = self.wage + increased_value
        print(f"Employee's salary increase {self.lastname} is {increased_value} ron."
              f"After the increase, his salary is {self.wage} ron.")
        print()

emp1 = Employee("Filipescu", "Marcu", 6000)
emp1.describe()
emp1.complet_name("I")
emp1.monthly_wage()
emp1.anual_wage()
emp1.increased_wage(24)
emp2 = Employee("Iliescu","Vladimir", 1000000)
emp2.describe()
emp2.complet_name("P")
emp2.monthly_wage()
emp2.anual_wage()
emp2.increased_wage(140)
print()


#4.Class Bank account.
# Attributes: iban, account_holder, balance.Constructor for all attributes
# Methods:
#  display_sold() - Account holder x has in account y the amount of n ron.
#  debit_account(amount)
#  credit_account(amount)

class Account:
    iban = None,
    account_holder = None,
    sold = None,
    def __init__(self, iban, account_holder, sold):
        self.iban=iban
        self.account_holder=account_holder
        self.sold = sold

    def describe_sold(self):
        print(f"The holder {self.account_holder} has in his account {self.iban} an amount of money of"
              f" {self.sold} ron")

    def debit(self, amount):
        if  self.sold < amount:
            print(f"Insufficient funds, check balance before withdrawal.")
        elif amount % 10 !=0:
            print(f"The amount withdrawn should have been a multiple of 10.")
        else:
            amount_rem = self.sold - amount
            print(f"Your post-withdrawal balance is {amount_rem} ron.")

    def credit(self, amount):
        self.sold +=amount
        print(f"Your balance after loading is {self.sold} ron")


cont1 = Account("ROBZRT237123892", "Vasilescu Mihai", 2132222)
cont1.describe_sold()
cont1.debit(23230)
cont1.credit(567789)
cont2 = Account ("ROZNTV6325363", "Bon jovi", 23450000)
cont2.describe_sold()
cont2.debit(4560000)
cont2.credit(300000000000)
print()

#5.Bill class
# Attributes: series (will be constant, no constructor needed, all invoices will
# have the same series), number, product_name, quantity, invoice_price
# Constructor: all attributes, no series

from datetime import date
from tabulate import tabulate
class Bill:
    series = "jdm"
    number = None
    product_name= None
    quantity = None
    unit_price =None


    def change_quantity(self, quantity):
        self.quantity = quantity
    def change_product_name(self, product_name):
        self.product_name = product_name
    def change_unit_price(self, unit_price):
        self.unit_price = unit_price
    def generate_bill(self,):
        print(f"The bill with the series {self.series} and number {self.number}.")
        print(f"From {date.today()}")
        print(tabulate({"Product_name": [self.product_name],
                        "Quantity": [self.quantity],
                        "Unit price ": [self.unit_price],
                        "Total price":[self.quantity*self.unit_price]},headers = "keys"))


bil1 = Bill()
bil1.change_quantity(15)
bil1.change_product_name('tablets')
bil1.change_unit_price(1200)
bil1.generate_bill()
bil2 = Bill()
bil2.change_quantity(26)
bil2.change_product_name("TV")
bil2.change_unit_price(1600)
bil2.generate_bill()
print()

#6.Car Class
# Attributes: make, model, top speed, current_speed, color,
# available_colours (set), registration (bool)
# Colour = grey - all cars when they leave the factory are grey
# Current_speed = 0 - all cars stand still when leaving the factory
# Available colors = you choose 5-7 colors
# Brand = you choose - factory produces one brand but several models
# Registered = False
# Constructor: model, max_speed

class Car:
    brand = "Toyota"
    model = None
    max_speed = None
    actual_speed = 0
    color = "gri"
    regist = False
    available_color = {"red", "blue","white","green","brown","black","yellow"}

    def __init__(self,model,max_speed):
        self.model = model
        self.max_speed =max_speed

    def describe_car(self):
        print(f"I want to show you my car {self.brand}, model {self.model}, painted in the color {self.color} "
              f" , which can reach a speed of {self.max_speed} km/h, but now we have a speed of"
              f" {self.actual_speed} km/h, and the registration is {self.regist}.")

    def regist_car(self):
        self.regist = True
        print(f"The car {self.model} is registered ? - {self.regist}.")


    def paint_car(self, color):

        if color in self.available_color:
            self.color = color
            print(f" The new color of the my car {self.model} is {self.color}.")
        else:
            print(f"The color you chose is not available, chose another color "
                  f"from the list {self.available_color}.")

    def acce_car(self,acc_value):
        if acc_value <0:
          print( "You have to speed up.")
        elif acc_value + self.actual_speed > self.max_speed:
            self.actual_speed = self.max_speed
            print(f"You can't go more then {self.max_speed} km/h.")
        else:
            self.actual_speed = acc_value
            print(f"You have accelerated to {self.actual_speed} km/h .")

    def slow_down(self):
        self.actual_speed = 0
        print(f"The car {self.model}  is stoped, the actual speed is: {self.actual_speed}.")
        print()


car1= Car("Yaris", 200)
car1.describe_car()
car1.paint_car("red")
car1.acce_car(140)
car1.regist_car()
car1.slow_down()

car2 = Car("Hilux", 180)
car2.describe_car()
car2.paint_car("green")
car2.acce_car(50)
car2.regist_car()
car2.slow_down()
print()

#7.TodoList class
# Attributes: todo (dict, key is task name, value is description)
# At first we have no tasks, dict is empty and we don't need a constructor

class TodoList:
    todo = {}

    def task(self, name, describe):
        self.todo[name] = describe

    def end_task(self, name):
        if name not in self.todo.keys():
            print(f"The task {name} is not in the To-do list")
        else:
            self.todo.pop(name)

    def display_todo_list(self):
        print(f"The remaining tasks are: ", end='')
        print(', '.join(self.todo.keys()))

    def display_info(self, name_task):
        global user_choice
        if name_task in self.todo.keys():
            print(f"The details of the  {name_task} task are: {self.todo[name_task]}")
        else:
            user_choice = input((f"This task is not in the Todo list! You want to add him to the list?(y/n) "))
        if user_choice.lower() == 'y':
            description = input(f"Please enter the description for the new task! : ")
            self.todo[name_task] = description

task1 = TodoList()
task1.task("testing", "test tha web page")
task1.end_task("testing")
task1.display_todo_list()
task1.display_info("test something")





