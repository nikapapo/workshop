# Numbers
#===========================

#Integers
num_int = 5
#print(type(num_int))

# Float
num_float = 5.35

# Type conversion

str_int = int("3")
#print(type(str_int))
str_float = float("3.25")

# Strings
#=============================
str_one_line = "Marcel is new kid in town"

str_multi_line = """ one
two
three
"""
# rogorc davwert ise dabechdavs 


# STRINGS METHODS
#--------------------------

s = "Python"
ss = "I have two cats"
#print(len(s)) length of the string
#print(s.upper())
#print(ss.title())

# REPLACE PARTS OF THE STRING
#print (ss.replace("cats","dogs"))
#ss = ss.replace("cats","dogs")

# SPLIT
#print (ss.split('a', 1))

#CONCATINATION
#=============================

#in Python you can concatinate only strings
concat = str(3) + "3"
#print(concat)

name = "Marcel"
age = 27

phrase =  name + " is " + str(age) + "years old"

phrase = f"{name} is {age} years old"# format strings
phrase = "{} is {} years old".format(name, age)#same thing
#print (phrase)

# BOOLEANS & NULLS
#===============================

b_true = True
b_false = False
b_null = None

# COLLECTIONS (ARRAYS)
#======================================

#LISTS(array in JS) cvladia
lst = [1,2,3,4]
#print( lst[1] )

# DICTIONARY cvladia
#===============

d = {
  "first_name": "Marcel",
  "last_name": "Duchamp",
  "age": 27
}
#print (d["first_name"])

# TUPLES ucvlelia, konstantaa
#=======================
t = ("apple", "car", 56)
#print(t[1])

# SET
#==============
s1 = { "apple", "car", 88}
s2 = { 54,3,59,5,99}
#print(s2)













