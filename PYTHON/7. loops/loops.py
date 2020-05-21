# LOOPS
# ================================================
# To test our loops, some values :
num_max   = 10
counter   = 0

name_list = ["Marcel", "Mary", "Dolores", "John"]
num_list = [1,2,3,4,5,6]
letters   = "Python"



# LOOPS ANATOMY
# -------------------------------------
# for item in letters:
#     print(item)

# while True:
#     print("While")
#     break


# LOOPS TESTS
# -------------------------------------
# THE FOR LOOP
# for num in num_list:
#     print(num)

# for num in range(1, 10 + 1):
#     print(num)



# THE WHILE LOOP
# while counter < num_max:
#     counter += 1
#     print(counter)

while True:
    if(counter < num_max):
        counter += 1
        print(counter)
    else:
        break