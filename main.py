import time
import cProfile
import pstats
def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

def adding(a,b):
    tempa=a
    tempb=b
    tempc=tempa+tempb
    return tempc

def waste_time():
    time.sleep(2)
    print("awake")

with cProfile.Profile() as profile:
    print("hello")
    print(adding(1023,8037))
    print(fact(20))
    waste_time()

results=pstats.Stats(profile)
results.sort_stats(pstats.SortKey.TIME)
results.print_stats()
# results.dump_stats("results.prof")