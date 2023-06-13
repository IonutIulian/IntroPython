
# Variables and Data Types

'''
A variable is a container in memory that stores values.Variables have a unique name
 so that they can be identified and used later.
The variable is created when we assign a value to it.
Variables start with a lowercase letter but can contain digits.
Variables are case sensitive.
Variables can change their value during program execution.
'''

#1.Declare and initialize one variable of each of the following types:

#string
car = "Volvo"
# int
year = 2017
#boolean
registered = True
#float
fuel_consumption = 6.7

#2.Use the type function to check if they have the expected data type.

print(type(car))
print(type(year))
print(type(registered))
print(type(fuel_consumption))

#3.Round the float using the round() function and save this change in
# same variable (override):

fuel_consumption = round(fuel_consumption)
print(type(fuel_consumption))

#4.Use print() and print 4 sentences to the console using the 4 variables.

print(f"-What car do you drive?"
      f"-I drove a {car}, it's a {year} model year.")
print(f"-Is it registered on your name?"
      f"-{registered} ")
print(f"-How much fuel your car consumes?"
      f"-It is consuming {fuel_consumption} litres of fuel per 100 kilometres")

#5.Read from the keyboard:
#- name;
#- first name.
#- Display how many characters the full name has.

name = "Petrescu"
first_name = "Florin"
print(f" The full name has {len(name+first_name)} characters")

#6.Area of a rectangle.

length =5
width=3
print(f"The area of the rectangle is {length*width} square metres.")

#7. Displays how many times the word 'the' appears;

sent = "Coral is either the stupidest animal or the smartest rock."
print(f"The word 'the' appears for {sent.count(' the ')} times.")

#8.Use an assert to check if this string contains only numbers.

#assert sent.isnumeric(), "Error, it is not"

#9.Displays the  middle character of a string.

text = "character"
middle = text[len(text)//2]
print(f"The  middle character is {middle}")

#10.Using assert, check if a string is a palindrome.
'''
str = "rotator"
rev = ''.join(reversed(str))
assert str == rev,"Error the string is not palindrome"
'''
#11.Saves each word in a variable; prints both variables for verification.

nstr = "banana orange"
spl = nstr.split()
print(spl[0])
print(spl[1])

#12.Capitalizes a character from a string everywhere except for the first and last
#character.


txt = "abracadabra"
print(txt[0]+txt[1:len(txt)-1].replace(txt[0],txt[0].upper())+txt[len(txt)-1])

#13.

user = "John"
password = "secret"
print(f"The password for user {user} is {'*'* len(password)} and has {len(password)} characters.")
