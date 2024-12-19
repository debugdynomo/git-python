import time

myTime=int(input("Enter the time : "))

for x in range(myTime,0,-1):
    sec=(x % 60)
    minutes=(x // 60) % 60
    hours=(x // 3600)
    print(f"{hours:02}:{minutes:02}:{sec:02}")
    time.sleep(1)
print("Time's up")