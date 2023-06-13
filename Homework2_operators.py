
#Operators & Data Types

#1.The if-else statement is used to execute both the true part and the false part of a given condition.
# If the condition is true, the if block code is executed and if the condition is false,
# the else block code is executed.
# When we want to execute more than two instructions we also enter an elif,
# which evaluates another condition that if found true will execute a set of instructions.
# If this condition is also false, it will go on to another elif evaluation or an else.

#2.Check and display whether x is a natural number or not.
'''
x = input("Choose a number:")
if x>0 and type(x) == int:
    print(f"The number {x} is natural number.")
else:
    print(f"The number {x} is  not a natural number.")
'''
#3.Check and display whether y is a positive, negative or neutral number.

'''
y = int(input("Choose a number:"))
if y >0:
    print(f"The number {y} is positive number.")
elif y<0:
    print(f"The number {y} is negative number.")
else:
    print(f"The number {y} is neutral number.")
'''
#4.Check and display if z is between -2 and 13.
'''
z = int(input("Choose a number:"))

if z >= -2 and z <= 13:
    print(f"The number {z} is between -2 and 13.")
else:
    print(f"The number {z} is not between -2 and 13.")
'''
#5.Check and display if the difference between p and t is less than 5.
#The abs function will be used.

'''
p = int(input("First number"))
t = int(input("Second number"))

if abs(p-t)<5:
    print(f"The difference between p and t is {abs(p-t)}, so less then 5.")
else:
    print(f"The difference between p and t is {abs(p-t)}, so  more then 5.")
'''

#6.Check if g is NOT between 5 and 27, including range ends.

'''g = int(input("Number:"))

if not(g >= 5 and g <= 27):
    print(f"The chosen number does not fit in the desired range ")
else:
    print(f"The chosen number is in the desired range ")'''

#7.Displays if k and l are equal, if not, displays which is bigger.

'''k = int(input("Number1:"))
l = int(input("Number2:"))

if k == l:
    print(f"The numbers are equal.")
elif k > l:
    print(f"Number1 is bigger than Number2.")
else:
    print(f"Number2 is bigger than Number2.")'''

#8.Assuming that a, b, c (all of type int) - represent the sides of a triangle, show whether
#the triangle is isosceles (two sides are equal), equilateral (all sides are equal) or
#random (no sides are equal).

'''a = int(input("Side1:"))
b = int(input("Side2:"))
c = int(input("Side3:"))

if a == b ==c:
    print("All sides are equal the triangle is equilateral.")
elif a == b or b == c or a == c:
    print("Two sides are equal the triangle is isosceles.")
else:
    print("All sides are different the triangle is random.")'''

#9.Read a letter from the keyboard then check and display whether it is a vowel or not. Attention!
#You need to evaluate uppercase and lowercase cases.

'''q = input("Choose a letter:")

if q.lower() in ('a','e','i','o','u'):
    print(f"The letter you chose is a vowel.")
else:
    print(f"The letter you chose is a consonant.")'''

#10.Transform and print school grades from Romanian system to American system.
'''
ro_grades = int(input("The student's grade is:"))
us_grades = ""

if ro_grades >=9:
    us_grades = "A"
    print(f"The student's grade is {us_grades}.")
elif ro_grades >= 8:
    us_grades = "B"
    print(f"The student's grade is {us_grades}.")
elif ro_grades >= 7:
    us_grades = "C"
    print(f"The student's grade is {us_grades}.")
elif ro_grades >= 6:
    us_grades = "D"
    print(f"The student's grade is {us_grades}.")
elif ro_grades >= 4:
    us_grades = "E"
    print(f"The student's grade is {us_grades}.")
else:
    us_grades = "F"
    print(f"The student's grade is {us_grades}.")
'''

# 11. Check if x has at least 4 digits.Check if x has exactly 6 digits.Check if x is even or odd
'''

x = int(input("number ="))
if x > 999:
    print(f"{x} has at least 4 digits")
else:
    print(f"{x} has less then 4 digits")


if x > 99999 and x <1000000:
    print(f"{x} has  exactly 6 digits")
else:
    print(f"{x} the number does not have exactly 6 digits")


if x % 2 == 0:
    print(f"{x} is an even number")
else:
    print(f"{x} is an odd number")'''

# 12. Having three variables x, y, z (all int) displays in the console which is the larger of
# them.
'''
x = int(input("first no ="))
y = int(input("second no ="))
z = int(input("third no ="))

if x > y and x > z:
    print(f"{x} is the bigger number")
elif y > x and y > z:
    print(f"{y} is the bigger number")
elif z > x and z > y:
    print(f"{z} is the bigger number")
else:
    print("The numbers are equal")
'''

#13. Assuming that x, y, z - represent the angles of a triangle, check and display whether
#the triangle is valid or not (a triangle is valid if the sum of all angles is 180 degrees)
'''
x = int(input("first angle ="))
y = int(input("second angle ="))
z = int(input("third angle ="))

if x + y + z == 180:
    print("The triangle is valid")
else:
    print("The triengle is not valid")
'''

#14.With the string: 'Coral is either the stupidest animal or the smartest rock' read by
# the keyboard a number x of type int and displays the string without the last x characters.
#Declare a new string to be the first 5 characters + the last 5.
#Save to a variable and displaythe starting index of the word rock, displays the whole string up to this word.

'''string = "Coral is either the stupidest animal or the smartest rock"

print(string[:len(string)-7])

new_string = (string[:5] + string[-5:])

print(new_string)
excw = "rock"
indx = string.index(excw)
print(string[:indx])'''

# 15.Read a string from the keyboard and check if the first and last characters are the same. You
# will use an assert.

'''string = input("type a string:")
assert string[0].lower() == string[-1] ,"Error, the letters are not the same."'''

#16.Having the string '0123456789' displays only even numbers and then only odd numbers.

'''string = "0123456789"

print(string[::2])
print(string[1::2])'''

#17.We want to create an application for purchasing airline tickets that will receive the right
# the following information:
# a. Age
# b. Accompanied by mother
# c. Accompanied by father
# d. Passport
# e. Mother's permission document
# f. Permission document father
#
# age = int(input("Your age is:"))
# passport = (input("You have a passport? "))
# with_mother = (input("Accompanied by mother?"))
# with_father = (input("Accompanied by father?"))
# perm_mother = (input("Mother Permission Act?"))
# perm_father = (input("Father Permission Act?"))
#
# if (age >= 18 and passport == "yes"):
#     print("You can board the plane")
# elif( age < 18 and with_father == "yes" and with_mother =="yes" and passport == "yes"):
#     print("You can board the plane")
#
# elif(age < 18 and with_father == "yes" and perm_mother == "yes" and passport == "yes"):
#     print("You can board the plane")
# elif (age< 18 and with_mother=="yes" and perm_father =="yes" and passport == "yes"):
#     print("You can board the plane")
# else:
#     print("You can't bord the plane is you don't meet the requirements"
#           "- you have a passport and you are above 18"
#           "- you have passport, you are under 18 but you are with both parents"
#           "- you have passport, you are under 18, you are with just one of your parents,"
#           "but you have a permit from the other parent.")

#18. Gambling game.
import random

dice_roll = random.randint(1,6)
my_number = int(input("Choose your lucky number: "))
if dice_roll == my_number:
    print(f"You win, the number you picked is equal to the number given by the dice: {dice_roll} == {my_number}")
elif dice_roll > my_number:
    print(f"You lost, the number you picked is smaller then the number given by the dice: {dice_roll} > {my_number}")
else:
    print(f"You lost, the number you picked is bigger then the number given by the dice:{dice_roll} < {my_number}")






