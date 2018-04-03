import sys
import time
print(sys.version)
print(sys.path)
print('Memonization Example')
cache = {}
def expensive_func(num):
    if num in cache:
        return cache[num]
    time.sleep(1)
    result=num*num
    cache[num]=result
    return result

print(expensive_func(10))
print(expensive_func(10))
print(expensive_func(10))
print(expensive_func(20))
