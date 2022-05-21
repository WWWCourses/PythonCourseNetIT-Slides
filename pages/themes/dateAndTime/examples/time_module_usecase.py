import time
from functools import reduce

#start timer
start = time.time()

# do some time intensive stuff:
sum = reduce(lambda x,y:x+y, range(1,1_000_001))
print("The sum of numbers from 1 to 1_000_000 is: ", sum)

#end timer
end = time.time()

print("[Finished in {:.6f}s]".format(end - start))

#The sum of numbers from 1 to 1_000_000 is:  500000500000
#[Finished in 0.087371s]
