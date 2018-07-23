import random

dice = ("heads","tails")
val = random.choice(dice)

count = 0
try_h = 1
while count <= 1000000:

    #print("count is: ",count)
    val = random.choice(dice)
 
    if val == "heads":
       if try_h >= 20: 
          print("YESS!!!!!!! it took: ", try_h , " trys")
       try_h = 1 
    
    else:
        #print(val)
        try_h = try_h + 1 
    
    count = count + 1
    
