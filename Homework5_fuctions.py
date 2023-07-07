
# HOMEWORK.5 - FUNCTIONS
# An area of code with a little logic of its own, which can be used/reused (called) by any number of
# times we need it. The advantage of using functions is the economy of code.
# Parameters are the input to functions, when the function needs it.


import math


#1.Function to calculate and return the sum of two numbers

def sum_of2(a,b):
    print("1.")
    sum = a +b
    return sum
print(f"The sum of the 2 numbers is: {sum_of2(20,54)}")

#2.Function to return TRUE if a number is even, FALSE for odd

def even_odd(c):
    print("2.")
    if c % 2 ==0:
        return True
    else:
        return False
print(even_odd(5))

#3.Function that returns the total number of characters in your full name.

def carac_name(last, first, middle):
    print("3.")
    a = len(last+first+middle)
    return a

print(f"My name has  {carac_name('Hagi', 'Cristiano','Adriano')} characters")

#4.Function that returns the area of the rectangular.


def rectangular_area(L,l):
    print("4.")
    area = L*l
    return area

print(f"The area of the rectangular is {rectangular_area(15,11)} square metres")

#5.Function that returns the area of the circle.

def circle_area(r):
    print("5.")
    area = r**2 *math.pi
    return area

print(f"The area of the circle is {circle_area(90)} square metres")

#6.Function that returns True if a character is found in a string and False if is not.

def character(string, b):
    print("6.")
    if b in string:
        return True
    else:
        return False

print(character('aloha amigo', 'p'))

#7.Function without return, gets a string and displays:
#- the number of characters in lowercase
#- the number of characters in uppercase

def upper_lower(string):
    print("7.")
    upp = 0
    low = 0
    for p in string:
        if p.isupper():
            upp += 1
        else:
            low +=1


    print(f"The number of characters in lowercase is {low}")
    print(f"The number of characters in uppercase is {upp}")
upper_lower('AM fost LA BUcuresti la paradA')

#8.Fuction that gets a list of numbers and returns a list with only positive numbers.

def list(numbers):
    print("8.")
    list_pozitive = []
    for cif in numbers:
        if  cif > 0:
            list_pozitive.append(cif)

    return list_pozitive

print(f"The list of positive numbers is {list([1,4,5,7,4,334,0,-12,-2,-4,0,34,36,67])}")

#9.Function that receives two numbers and displays fi the first number is bigger then the second,
# or the second is bigger then the firts,or the numbers are equal.

def comp_nr(x,y):
    print("9.")
    if x > y:
        print(f"The fisrt number is bigger then the second. {x}>{y}")
    elif y > x:
        print(f"The second number is bigger then the first. {y}>{x}")
    else:
        print("The numbers are equal.")

comp_nr(4,8)

#10.Function that receives a number and a set of numbers.
# displays 'we added new number to set' + returns True
# displays'did not add number to set. It already exists' +
# returns False

def set_no(set , no):
    print("10.")
    if no not in set:
        set.append(no)
        print("Added the new number to set.")
        return True
    else:
        print(f"Did not add the new number to set, it is already there.")
        return False


print(set_no([1,2,3,4,5,6],5))

#11.Function that receives a month of the year and returns how many days that month has.

import calendar
from calendar import monthrange
def month(t,r):
    print("11.")
    print(f"The number of days that the month of {r} has is : {monthrange(t , r)[1]}")

month(2024, 2)

#12.Calculator function to return 4 values. Addition, difference, multiplication, division of two numbers.

def calculator(a,b):
    print("12.")
    return (a+b, a-b, a*b, a/b)

a, b, c, d = calculator(10, 2)
print(f"Sum: {a}")
print(f"Difference: {b}")
print(f"Multiplication: {c}")
print(f"Division: {d}")

#13.Function receiving a list of digits.
# Returns a DICT that tells us how many times each digit appears.

def frequency(list):
    print("13.")
    freq = {}
    for no in list:
        if (no in freq):
            freq[no] += 1
        else:
            freq[no] = 1

    for key, value in freq.items():
        print("% d : % d" % (key, value))

if __name__ == "__main__":
    frequency([1, 3, 1, 5, 9, 7, 7, 5, 5])

#14.Function that receives 3 numbers. Returns the maximum value between them.
def maxim(a, b, c):
    print("14.")
    if (a >= b) and (a >= c):
        max = a

    elif (b >= a) and (b >= c):
        max = b
    else:
        max = c

    return max

print(f"The maximum of the three numbers is : {maxim(4,6,8)}")

#15.Function to receive a number and return the sum of all numbers from 0 to that number.

def add(q):
    print("15.")
    sumr = 0
    for i in range (q+1):
        sumr +=i
    return sumr
print(f"The sum of all numbers: {add(10)}.")

#16.Function that receives 2 lists of numbers and returns the common numbers.

def common(list1 , list2):
    print("16.")
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result


print(f"The list with common numbers is: {common([1, 1, 2, 3] ,[2, 2, 3, 4])}")

#17. Function to apply a price discount.
def disc(full_price, discount):
    print("17.")
    dis_price = 0
    if discount <0:
        print('Invalid discount')
    elif discount>=100:
        print('Invalid discount')
    else:
        dis_price = full_price - (full_price * discount/100)
        return dis_price


print(f"The price after the discount is {disc(200 , 50)} ron")

#18.Function to display how many days until Christmas.

from datetime import date

def days_to(date1, date2):
    print("18.")
    return (date2 - date1).days

date1 = date(2022, 12,2)
date2 = date(2022, 12, 25)
print(f" Days until Christmas: {days_to(date1, date2)} .")

#19.Function to display the current date and time in Romania and China

import pytz
from datetime import datetime

def country_time_zones():
    print("19.")
    Country_Zones =  ['Europe/Bucharest' ,'Hongkong' ]
    country_time_zones = []
    for country_time_zone in Country_Zones:
        country_time_zones.append(pytz.timezone(country_time_zone))
    for i in range(len(country_time_zones)):
        country_time = datetime.now(country_time_zones[i])
        print(f"The date in {Country_Zones[i]} is {country_time.strftime('%d-%m-%y')} "
              f"and the time is {country_time.strftime('%H:%M:%S')}")

country_time_zones()

#20. Appliyng a discount.
def price_calculation_after_discount (age, season, clas, price ):
    discount = 0
    if age > 65:
        discount = 0.15
    else:
        num_children = int(input("Please enter the number of children you are travelling with: "))
        if num_children > 0:
            discount = 0.1
    if season == 'winter':
        discount += 0.1
        if clas == 1:
            tax = 0.03
        else:
            tax = 0.01
    price = price - price * discount + price * tax
    return price

age = int(input("Please enter your age : "))
season = input("Please enter the season when you travel: ")
clas = int(input("Please enter the class in which you are travelling: "))
price = int(input("Please enter the basic ticket price: "))


pret_calculat = price_calculation_after_discount (age, season, clas, price )
print(f"The price after the discount is:{pret_calculat}")

