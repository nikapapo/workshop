#1.Is the Number Less than or Equal to Zero   
#========================================================  
def less_or_equal(input):
    if ( input <= 0 ):
       return ("True!")
   
    else :
       return ("False!")

#print(less_or_equal(5))
#print(less_or_equal(0))

#2. Is the Number Even or Odd?
#========================================================

#num = int(input("Enter a number: "))
 
#if (num % 2) == 0:
       #print("{0} is Even".format(num))
 
#else:
       #print("{0} is Odd".format(num))
#Second way

#def is_even_or_odd(input):
    #if ( input % 2 == 0 ):
       #return ("EVEN!")
   
    #else :
       #return ("ODD!")
  
#print (is_even_or_odd(5))


# 3.Is the Word Singular or Plural?
#===================================================

def is_plural(word):
    
    if ( word.endswith("s") ): 
       return ("Plural")
    
    else :
       return ("Singular")
  
#print(is_plural("dog"))


#4. A function that returns the area of a surface in m2
#===========================================================

def surface_in_m2 (a, b) :
    
    return (a* b)
#print( surface_in_m2(5,5))



# 5. Returns the Remainder from Two Numbers
#================================================

def remainder (x,y) :

    return ( x % y)

#print (remainder(28,12))


# 6. Extract City Facts
#=============================================





# 7. Calculate the Profit
#================================================

def profit(costPrice, sellPrice, inventory): 
   
    totalSales = inventory * sellPrice
   
    totalCost = inventory * costPrice
   
    return (totalSales - totalCost)
  
#print(profit(2.5,4.5,50))



# 8. Is today Tuesday
#===================================================

import datetime

weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
current_weekday = current.datetime

def my_day (current_weekday):
  if current_weekday == weekDays[1]:
    return("Yes, It is a Tuesday")
  else :
    return ("Nope, You are wrooong!")

print(my_day)

#NOT DONE !! WILL DO :)))) LAST ONE DOESN'T WORK