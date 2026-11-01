# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 23:25:29 2026

@author: M&N
"""

"""
set 

"""

a = {1, "hossein"}
print(type(a))
a.add("ali")

print(a)

b = {2, "hasan","ali"}

print(a.union(b))

print(a.difference(b))

print(a.intersection(b))

print("ali" in a)


a.update([2, "reza"])

print(a)
print(len(a))


a.remove(2)
print(a)

a.discard("ali")
print(a)

c = a.pop()

print(c)

h = a.copy()
print(h)

a.clear()
print(a)


s = {1, 2, 3, 8}

f = {4, 5, 6, 8}

print(s-f)
print(s.union(f))
r = s.difference(f)
print(r)
print(s.symmetric_difference(f))
print(s^f)

print(s.intersection(f))

print(s&f)


x = {56, 98 }
s = 'ali'
a = [13, 25 ]
t = (7, 8 )
d = {'one':1 , 'two':2}
x.update(s,a,t,d)         #{98, 7, 8, 'one', 13, 'l', 'a', 'two', 56, 25, 'i'}
print(x)

print("=====================================")


numbers = {1, 2, 3, 4}

numbers.add(10)

print(numbers)

print("=====================================")

numbers = {1, 2, 3, 4}

numbers.remove(2)

print(numbers)

numbers.discard(2)  #no erorr

print("=====================================")

languages = {"Python", "Java", "C++", "PHP"}

print("Python" in languages)


print("=====================================")
# tarkib
a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)

print(result)

print("=====================================")
# ashtrak
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.intersection(b)

print(result)

print("=====================================")

#اعضایی که فقط در a وجود دارند را پیدا کنید:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.difference(b)

print(result)

#حذف تکراری‌های List
numbers = [1, 2, 2, 3, 4, 4, 5, 5]

numbers_set = set(numbers)

print(numbers_set)

print("=====================================")


#بررسی کنید آیا a زیرمجموعه b است یا خیر:
a = {1, 2}
b = {1, 2, 3, 4}

result = a.issubset(b)

print(result)

print("=====================================")

python_class = {
    "Ali",
    "Sara",
    "Reza",
    "Hossein"
}

ai_class = {
    "Sara",
    "Reza",
    "Mohammad"
}

#دانشجو مشترک
common = python_class.intersection(ai_class)

print(common)

#تمام دانشجو ها

all_students = python_class.union(ai_class)

print(all_students)

#فقط دانشجویان پایتون

only_python = python_class.difference(ai_class)

print(only_python)

#فقط دانشجویان ai





