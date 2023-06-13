

#DATA STRUCTURES

# Data structures are memory addresses that can store multiple values
# 1.Lists
#    represent non-homogeneous memory addresses that can store values with different data types.
# Each element in the list has an index starting from 0 (like the string).
# The list is ordered, so when we add a new element, it will be put at the end.
# The list is mutable, i.e. we can add, delete or change elements in it.
# # In the list we can put duplicate values and len() will give us the size of the list.

# 2. The  sets
# Represents data structures that hold multiple unique values in a variable without being ordered or indexed.
# Because of this they are also immutable (we cannot change the location of elements).
# We can only add or delete elements.We can use len() to find out the size.

# 3. Tuples
#    Represents ordered and identifiable index-based data structures that accepts duplicates and is immutable.
# Can't add or delete values, we can use len() to find out the size.

# 4. Dictionaries
# Are data structures that store data of type key : value. They are ordered, mutable, so values can be changed.
# Keys are unique, we can't have duplicate keys, it would create confusion.Keys are like nicknames for indexes.
# We can use len() to find out the size.

#1.Declare a list of musical notes

# musical_notes = ["do","re","mi","fa","so","la","si","do"]
# print(f"Musical notes: {musical_notes}")
# #Reverse the order using slicing and overwrite this list,
# musical_notes = musical_notes[::-1]
# print(musical_notes)
# # Reverse again
# musical_notes.reverse()
# print(musical_notes)
# #Display on the screen how many times the note 'do' appears in the list.
# print(f"The note 'do' appears {musical_notes.count('do')} times.")

#2.Having 2 lists, [3, 1, 0, 2] and [6, 5, 4], find 2 variants to merge them into one list.

# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]
# #first variant
# list3 = list1 +list2
# print(f"First variant: {list3}")
# # second variant
# list2.extend(list1)
# print(f"Second variant: {list2}")
# # Sort the resulting list
# list3.sort()
# print(f"The sorted list is: {list3}")
# list3.remove(0)
# print(list3)

#3.Using an if, check if the list generated in exercise 2 is empty or not.

# if not list3:
#     print("The list is empty")
# else:
#     print(f"The list is not empty {list3}")

#4. Empty the list from the previous exercise.
# list3.clear()
# print(list3)

#.5 Having dictionary dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, use a function to
#display Students (keys)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(f"The students attending are : {dict1.keys()}")

#.6 Print the 3 students from the dictionary above and their respective grades.

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
for key in dict1.keys():
    print(f"{key} got a {dict1[key]}")

#7. Changing Dorel's grade.
dict1['Dorel']= 6
print(f"Dorel's grade is now {dict1['Dorel']}")

#8.Gigel transfers out of class and a new classmate named Ionica comes in.
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(f"Students in this class are {dict1}")

#9. We have the following sets.

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(f"Days of the week{zile_sapt}")

#10.Check if weekend is a subset of zile_sapt.

if weekend.issubset(zile_sapt):
    print("Weekend is a subset of zile_sapt")
else:
    print("Weekend is not a subset of zile_sapt.")

#11.Display the differences between these 2 sets.
print(f"The differences between these 2 sets are : {zile_sapt.difference(weekend)}")

#12.Show the intersection of the elements in these 2 sets.
print(f"The intersection of the elements in these 2 sets is {zile_sapt.intersection(weekend)}")


#13.We imagine a football team during the match.
# A maximum of 3 changes are allowed.
# Play with different values to see how the data goes through the code.

field_players = ["ion", "sebi","adi","alex","geo"]
bench_players = ["marcel","vali","gicu","mirel","dan"]
CHANGES = 3
changed_players= []
changes_done = 0

if changes_done == CHANGES :
    print("No more changes available")
else:
    while changes_done != CHANGES:
        print(f"Players on the field: {field_players}")
        print(f"Available changes {CHANGES-changes_done}")
        print(f"Players on the bench: {bench_players}")
        print(f"Changed players: {changed_players}")
        changed_player = input("Choose the players you want to change: ")
        if changed_player not in field_players:
            print(f"The player is not on the field")
        else:
            changes_done += 1
            field_players.remove(changed_player)
            changed_players.append(changed_player)
            print(f"The player {changed_player} will be changed.")
            player_entered = input("Choose the player you want to add: ")
            if player_entered not in bench_players:
                print(f"The player is not on the bench")
            else:
                bench_players.remove(player_entered)
                field_players.append(player_entered)

                print(f"The player {player_entered} will join the field")
                print(f"You have {CHANGES - changes_done} changes left.")

        if CHANGES == changes_done:
            print(f"Players on the field {field_players}")
            print("You've made all available changes")










