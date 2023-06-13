

# Homework 4 - Repetitive Cycles

#1. Use a forum to browse through the whole list and display;
# 'My favourite car is x'.
# Do the same with a for each.
# Do the same with a while.

cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun',
'Fiat', 'Trabant', 'Opel']

for i in range (len(cars)):
    print(f"My favourite car brand is {cars[i]}")

print()

for car in cars:
    print(f"My favourite car brand is {car}")

print()

i=0
while i <= len(cars)-1:
    print(f"My favourite car brand is {cars[i]}")
    i=i+1

#2. Changes the items in the list so that they are written in capital letters,
#except for the first and last.

for i in range(len(cars)):
    if i > 0 and i < len(cars) - 1:
        cars[i] = cars[i].upper()
else:
    print(f'The list of capitalised car brands is: {cars}')

#3.A buyer comes in looking to buy a Mercedes.
# Look through the list in the way you choose.

for car in cars:
    if car == 'MERCEDES':
        print(f"We found the car you want {car}")
        break
    else:
        print(f"This car is the brand {car}. We're still looking.")

#4. A rich but indecisive buyer comes in. We'll show him all the cars with the
# except of the Trabant and the Lastun.

excluded_cars = ['LASTUN','TRABANT']
for car in cars:
    if car in excluded_cars:
        continue
    print(f'You might like the car : {car}')

#5. Upgrade the fleet:
#  Create an empty list, old_cars.
#  Browse through cars.
#  When you find a Lăstun or Trabant:
#  Save these cars in old_cars.
#  Overwrite them with 'Tesla' (in the original list of cars).
old_cars = []

for i in range(len(cars)):
    cars[i] = cars[i].lower()
    if cars[i] in ['lastun', 'trabant']:
        old_cars.append(cars[i])
        cars[i] = 'tesla'
print(f"The list with old cars is : {old_cars}")
print(f"The list with new cars is : {cars}")

#6.A client comes with a budget of 15,000 euros.
#  Show only cars that fit into this budget.
#  Retrieve via dict.items() and access the car and price.
#  Print For a budget under 15000 euro you can choose the car:
#  Retrieve via list.

car_prices = {
'Dacia': 6800,
'Lastun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
avail_money = 15000
for keys , value in car_prices.items():
    if value <=avail_money:
        print(f"The cars that you can afford are : {keys}")


#7.Having the list:
#  Go through it.
#  Show how many times the number 3 appears in the list (you are not allowed to use count).
count = 0
list = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for cif in list:
    if cif == 3:
        count += 1
print(f"The number 3 appears in the list  {count} times.")

#8. Same list.Calculates and displays the sum of the numbers.

sum = 0
for i in range (0, len(list)):
    sum =sum +list[i]

print(f"The sum of the numbers from the list is : {sum}")

#9.Same list. Find the largest number from the list without using max fuction.
max = list[0]
for x in list:
    if x > max:
        max = x

print(f"The largest number from the list is {max}")

#10. Same list. If the number is positive, replace it with its negative value.


for i in range (len(list)):
    if list[i] > 0:
        list[i] = list[i] * -1

print(f"The list after the replace is: {list}")


#11.Correctly populates other lists
#Show the 4 lists at the end

rand_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []

for cif in rand_numbers:
    if cif % 2 == 0:
        even_numbers.append(cif)
    else:
        odd_numbers.append(cif)
    if cif > 0:
        positive_numbers.append(cif)
    else:
        negative_numbers.append(cif)
print(f"The even numbers are: {even_numbers}")
print(f"The odd numbers are: {odd_numbers}")
print(f"The positive numbers are: {positive_numbers}")
print(f"The negative numbers are: {negative_numbers}")

#12. SAme list. Sort the list in ascending order without using sort.

rand_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(rand_numbers)-1):
		for j in range(i+1,len(rand_numbers)):
				if rand_numbers[i]>rand_numbers[j]:
						swap = rand_numbers[i]
						rand_numbers[i],rand_numbers[j]=rand_numbers[j],rand_numbers[i]
						rand_numbers[j] = swap
print(f"The list sorted in asceding order is: {rand_numbers}")

#13.Number riddle:

# import random
# secret_numer = random.randint(1,30)
# guessed_number = None
# while guessed_number != secret_numer:
#     guessed_number = int(input("Chose a number between 1 and 30:"))
#     if secret_numer == guessed_number:
#         print(f"Congratulations you guessed it.")
#         break
#     elif secret_numer > guessed_number:
#         print(f"Chose a bigger number")
#     else:
#         print(f"Chose a smaller number")


#14.Choose a number from the keyboard
# Write a program to generate the following pyramid in the console
# 1
# 22
# 333
# 4444

Nr = int(input("Chose number : "))

for i in range(1,Nr+1):
    for j in range(1, i+1):
        print(i, end="")
    print()


#15.

phone_keypad = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]]
for i in range(len(phone_keypad)):
    for j in range(len(phone_keypad[i])):
        print(f"The current number is {phone_keypad[i][j]}")