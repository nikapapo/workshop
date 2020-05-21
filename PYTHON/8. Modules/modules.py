# MODULES (obieqtebi)
#=================================

# IMPORTING

#import math

# CREATE A ALISE FOR MODULE
#=======

#import math as m 

#print(dir(m) )# gachvenebs ra funqciebi(metodebia) shignit

#mf = m.floor(5.45)
#print(mf)# qveda machvenebeli,"ceil" zeda mach


# YOU CAN IMPORT ONLY THE METHOD YOU NEDD
#=============================

from math import ceil,floor # zaan magaria


mc = ceil(5.45)
#print(mc)


# IMPORT CUSTOM MODS AND METHODS

from Mymod import printus

#printus(3*3)


#  TIME MODULE
#============================
import time 

#local = time.localtime()
#print(local)


#def calc_age(birth_year,int) :

    #user_val = input("your birth year")

    #if not user_val.isnumeric() : return "we need "
    #return local.tm_year - int(user_val)
    
    #if(isinstance(birth_year,int)):
      #return local.tm_year -birth_year
    #else:
      #return "we need a integer"

#time.sleep(5)


#print ( calc_age() )
