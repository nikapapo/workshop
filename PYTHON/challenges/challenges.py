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




# 6. Calculate the Profit
#================================================

def profit(costPrice, sellPrice, inventory): 
   
    totalSales = inventory * sellPrice
   
    totalCost = inventory * costPrice
   
    return (totalSales - totalCost)
  
#print(profit(2.5,4.5,50))



# 7. Is today Tuesday
#===================================================

#import time


#today = time.strftime("%A")

#if today == "Tuesday" :
  # print ("Yes, today is Tuesday")

#else:
 #  print ("No, it is not Tuesday")


# 8.Equality of 3 Values
#=============================================


def equality(a,b,c):

    if (a == b) and (a==c):
        return (3)
    elif (a == b) or (a==c) or (b==c):
        return (2)
    else :
        return(0)
print(equality(5,3,2))



# That's all , I think ...:)))















