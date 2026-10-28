# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 23:52:21 2026

@author: M&N
"""

"""
step 1

"""
pizza_price = 140
pizza_name = 12
dooghe_price = 400
dooghe_name = 6 
ja_price = 6000
ja_name = 3
kharje_kol = (pizza_price*pizza_name)+(dooghe_price*dooghe_name)+(ja_price*ja_name)
print(kharje_kol)

a = kharje_kol/3
print(a)

print('/n==========================')




test2 = "hossein"

print(type(test2))

test3 = 20

print(type(test3))


"""
step 2

"""
#print string

name = "Hossein"

city = "Tehran"

language = "Python"

print(name +"/ " + city + "/ " + language)

print('/n==========================')


age = 20

age2 = "20"

print("Python " * 3)

print('/n==========================')

#len string

name = "Python"

print(len(name))

print('/n==========================')


"""
index
Python

P   y   t   h   o   n

0   1   2   3   4   5
Python

-6 -5 -4 -3 -2 -1
"""

word = "Python"

print(word[0])

print(word[3])

print(word[-1])


print('/n==========================')



"""
slicing 

string[start:end]

"""
word = "Python"

print(word[0:3])

print(word[2:6])


print(word[:4])


print(word[2:])

print('/n==========================')


"""
metud

"""
name2 = "hossein"

print(name2.lower())

print(name2.upper())

print(name2.capitalize())

print(name2.index("o"))

text = "   Python   "

print(text.strip())

text = "I Love Java"

print(text.replace("Java","Python"))



"""
EX



#نام خود را دریافت کنید و تعداد حروف آن را نمایش دهید.

name = input("نام خود را وارد کنید: ")

print("نام شما:", name)
print("تعداد حروف:", len(name))


#نام و نام خانوادگی را دریافت کرده و کنار هم چاپ کنید.

first_name = input("نام: ")
last_name = input("نام خانوادگی: ")

full_name = first_name + " " + last_name

print("نام کامل شما:", full_name)



#کلمه Python را چاپ کنید و سپس حرف سوم آن را نمایش دهید.

word = "Python"

print(word)

print("حرف سوم:", word[2])
"""
print('/n==========================')



# جلسه دوم




name3 = "hossein"

last_name3 = "aziz"

age3 = 27

print("hello {} {} you are {}".format(name3, last_name3 , age3))

print("hello {1} {0} you are {2}".format(name3, last_name3 , age3))


print(f"hello {name3}  {last_name3}  you are {age3}")

print('/n==========================')



name = input("نام: ")
city = input("شهر: ")

print(f"سلام {name}")
print(f"شما اهل {city} هستید.")
print('/n==========================')


print("Python\nProgramming")


print('/n==========================')

print("نام\tسن")
print("علی\t20")
print("رضا\t22")

print("Name\tAge")
print("Ali\t20")

"""


رشته‌ها تغییرناپذیر هستند (Immutable)

text = "Python"
text[0] = "J"


TypeError


"""

#برای تغییر باید رشته جدید بسازیم.

text = "Python"
    
text = "J" + text[1:]
    
print(text)

print('/n==========================')


#عضویت در رشته

text = "Python Programming"

print("Python" in text)


print('/n==========================')


#عدم عضویت

print("Java" not in text)



#پایتون به حروف کوچک و بزرگ حساس است.

print("Ali" == "ali")

print('/n==========================')


#مثال کامل

first_name = input("نام: ")
last_name = input("نام خانوادگی: ")
age = int(input("سن: "))

print(f"سلام {first_name} {last_name}")
print(f"سن شما {age} سال است.")


print('/n==========================')



"""
✔ رشته داخل کوتیشن نوشته می‌شود.

✔ رشته و عدد متفاوت هستند.

✔ برای اتصال رشته‌ها از + استفاده می‌کنیم.

✔ برای تکرار رشته از * استفاده می‌کنیم.

✔ بهترین روش نمایش متغیرها استفاده از f-string است.

✔ رشته‌ها قابل تغییر مستقیم نیستند.

✔ پایتون به حروف کوچک و بزرگ حساس است.
"""

x = 'Hi this is a string'

# تبدیل به حروف کوچک
x = x.lower()

# تبدیل رشته به لیست
words = x.split()

print(words)


name = "Hossein"

first_s = name.find("s")
second_s = name.find("s", first_s + 1)

print(second_s)
print(name[second_s])


name5 = "mohammad"

family_name1 = "aziz"

print(f"hello {name5} {family_name1}")





































