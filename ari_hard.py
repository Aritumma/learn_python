import random

## A coin has head and tails - lets call it dice :) 
dice = ("heads","tails")
x = 20
## initialize 
count = 0
ctr = 0
try_h = 1

while count <= 10000000:

    #print("count is: ",count)
    val = random.choice(dice)
    #look for heads apearing back to back 
    if val == "heads":
       # if it happens more than X times, success! 
       if try_h >= x: 
          print("YESS!!!!!!! it took: ", ctr , " tosses to get " ,x, "heads  in a row")
          try_h = 0 #reset after success
          ctr = 0
       try_h = try_h + 1  # keep counting back-to-back heads
       
    else:
        
        try_h = 1 #reset if not heads
        ctr = ctr + 1
    
    count = count + 1
    
