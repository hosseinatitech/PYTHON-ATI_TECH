# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 00:07:49 2026

@author: M&N
"""

"""

list 

"""
my_list = [0, 1, 2, 3, 4, 5]

print(type(my_list))

print("/n---------------------")

# list ordered hast yani be tartib

my_list2 = ["hossein", "ali", "reza"]

print(my_list2)

print(type(my_list2))

print("/n---------------------")


my_list3 = [0, 1, 2, 3, 4, 5]

print(my_list3[4])

print(my_list3[4:])

print(len(my_list3))


print("/n---------------------")

print(my_list + my_list2)

print(my_list + my_list3)

print("/n---------------------")


new_list = my_list + my_list3
print(new_list)

print(len(new_list))

print("/n---------------------")

#print(my_list * my_list3) error


print(my_list * 2)

print("/n---------------------")

new_list2 = new_list.count(2)



print(new_list2)

print("/n---------------------")

list1 = [1, 2, 3, 4, 5, 6, 7]

list2 = list1.pop(2)
print(list2)

print(list1)

print(list1.pop())

print("/n---------------------")

name_list = ["hossein", "ali", "reza", "sara"]

name_list.sort()

print(name_list)

name_list[3] = "zahra"

name_list.remove("hossein")

print(name_list)

last_list = [5, 8, 9, 0, 1, 6, 4, 2, 3]

last_list.sort()
print(last_list)

last_list.reverse()
print(last_list)


names = ["Ali", "Sara", "Reza"]

print("Sara" in names)

print("hossein" in names)

"""
name2 = list(input("entee your list"))
name3 = list(input("enter your list"))

print(name2 + name3)             

name2.sort()


print(name2)

name2.reverse()

print(name2)

print(name2 + name3)  

"""


fruits = ["Apple","Banana","Orange"]

fruits[1] = "Mango"

print(fruits)










