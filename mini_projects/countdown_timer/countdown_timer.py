import time 
#import time module

my_time = int(input("Enter the time in seconds : "))

for x in range(my_time, 0, -1): #-1 is used to do same wrk are reversed fn.
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("WAKEY_WAKEY!")