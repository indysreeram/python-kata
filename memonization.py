import time
cache={}
def expensive_multiply(num):
    if num in cache:
        return cache[num]
    time.sleep(1)
    result =num*num
    cache[num]=result
    return result

print(expensive_multiply(10))
print(expensive_multiply(20))
print(expensive_multiply(10))
print(expensive_multiply(30))
print(expensive_multiply(10))
