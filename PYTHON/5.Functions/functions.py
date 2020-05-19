#BUILD IN FUNCTIONS
#=================================

#print function
#print("whatever")
#print("whatever","and","ever")

age = 12
#print("age is:", age)

# Max , Min, Round

l = [3,6,76,12]
#print( max(l))# this will show max value in list
# min will show minimal value in the list

num = 3.36546546546
#print (round(num, 1)) #amrgvalebs uaxloestan

# INPUT
#input_val = input("Please enter your birth year: ")
#calc_age = 2020 - int( input_val ) 
#print("Your age is:", calc_age)

# CUSTOM FUNCTIONS
#===========================================

def calc(x, y = 0):
    #pass # cariels ver davtovebt funqcias, ase rom droebit vcert pass
    return x + y # return amtavrebs funqcias
    
#print(calc(2)) es isev sheceuli unda ikos

# IMPORTING
#=============================

import time
#print( dir(time) )

local = time.localtime()
current_year = local.tm_year


#print(local.tm_year)


# CHALLENGE
  
def calc_age () :
    input_birth = input ("Birth year, please: ")
    return current_year - int(input_birth)

print(calc_age())