# -*- coding: utf-8 -*-
"""DIU_OOPII_lab4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TtBaJ2S1IuPtW9BwxoCVPvZYxxfFuq2t

# Deep Dive into sets in Python

A set is a unordered group of elements, where the elements themselves are immutable.

It may include elements of different types. This means you can have a group of numbers, strings, and even tuples, all in the same set!
"""

set1 = {19, 3, 2, 2, 13}
print(set1)

set2 = sorted({19, 3, 2, 2, 13})
print(set2)

set3 = {'James', 3, 2, 2,'Python'}
print(set3)

set4 = sorted({'James','Python','Mutton','Bag'})
print(set4)

# Will give error
# set5 = sorted({'James', 3, 2, 2,'Python'})
print(set5)

# Different types of set

set1 = {False, False, True}
print(set1)

set2 = {10.0, "Hi", (11, 12, 13)}
print(set2)

set3 = set([11, 12, 13, 2])
print(set3)

# How to Modify a Set in Python

# initializing a set
a = {11, 13}
print(a)

# adding an item
a.add(12)
print(a)

# adding multiple elements
a.update([22, 13, 14])
print(a)

# adding list and set
a.update([14, 15], {11, 16, 18})
print(a)

# How to Get the Length of a Set

cars = {"X", "Y", "ZZ"}
print(len(cars))

"""# Various Set Methods"""

x = {"pear", "grapes", "kiwi"}
x.add("orange") #used to add a single item to the set
print(x)

y = {"mango", "banana", "apple"}
x.update(y) #used to update the set with union of others and itself
print(x)

x = y.copy() #used to return a copy of the set
print(x)

x.clear() #used to remove all items of the set
print(x)

y.discard("banana") #used to remove an item from the set. If the item is not an element, then nothing is done
print(y)

z = x.union(y) #used to return a new set as a union of sets
print(x|y) #it also represents union operation
print(z)

w = x.intersection(y) #used to return a new set as a intersection of sets
print(x & y) #it also represents intersection operation
print(w)

z = x.difference(y) #used to return a new set as the difference of two or more sets
print(x-y) #The difference between two sets is the set of all the elements in first set that are not present in the second set.
print(z)

"""#Frozen Set
A new class having the characteristics of a set in python whose items
cannot be changes post assignment is known as Frozenset.

Like tuples behave as immutable lists, frozensets behave as immutable sets.

frozenset() function is used to create frozensets.

As they are immutable, add and remove item methide aren’t supported.
"""

#initialize frozenset a and b
a = frozenset([11, 12, 13, 14])
b = frozenset([23, 24, 25, 26])

print(a.isdisjoint(b)) #if the intersection of two sets is null, return true
print(a.difference(b))
print(a|b)

# a.add(10)

"""# Creating a Set from user Input in Python"""

# create a set from string user input
my_set = set(input('Enter space-separated words: ').split())
print(my_set)

#create a set from integer user input
user_input = input('Enter space-separated integers: ')
print(user_input)
print(type(user_input))
my_set = set(int(item) for item in user_input.split())
print(my_set)