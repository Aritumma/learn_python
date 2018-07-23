import random

dice = (1,2,3,4,5,6)
val = random.choice(dice)

count = 0
while count <= 100:

    print("count is: ",count)
    val = random.choice(dice)

    if val == 1 :
       print("NOOOOO!!!!!!! it is 1 ")

    if val == 6 :
       print("YESS!!!!!!! it is 6 ")

    else:
         print(val)
    
    count = count + 1
 
