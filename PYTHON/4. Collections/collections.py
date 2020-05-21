# LISTS
#====================================

arr = ["monkey","dog","snake","spider","zebra"]
#print (arr[1])

arr [1] = "cat"
#print(arr)


arr.append("horse") #amatebs boloshi
arr.pop(2) # cashli imas romelic ginda
#print(arr)
arr.remove("spider") #cashli imas romelis saxelic ici  
#print(arr)
arr.insert(1,"lion")
#print(arr)

#print(len(arr))#


# TUPLES konstantaa
#=========================================

tup = ("monkey","dog","snake","spider","zebra")

#print(tup[1])
tup = list(tup)
tup[1] = "cat"
tup = tuple(tup)
#print(tup) #  konvertacia , tu ramis shecvla ginda

# SORTIREBA
#==============================================

arr = ["monkey","dog","snake","spider","zebra"]
arr.sort(reverse=True)# ukugma bechdavs
#print(arr)

arr_nums = [8,95,21,1,6]
#print(min(arr_nums)) moqmedebs sityvebzec,,
#print(max(arr_nums))anbanis mixedvit shlis


# DICTIONARY
#========================================

person = {
      "first_name": "John",
      "last_name" : "Doe",
      "age"       : 21

 }
#print(person["first_name"], ["last_name"])


person["job"] = "web dev"
print(person)



