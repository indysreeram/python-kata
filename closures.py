def square(x):
    return x*x
def cube(x):
    return x*x*x
def my_map(func,args_list):
    results=[]
    for i in args_list:
        results.append(func(i))
    return results

f = square(10)
x = square
print('The value before square is '+str([1,2,3,4,5]))
squares=my_map(square,[1,2,3,4,5])
print('The value after square is  '+ str(squares))
print('The value before cube is '+str([1,2,3,4,5]))
squares=my_map(cube,[1,2,3,4,5])
print('The value after cube is  '+ str(squares))

print(square)
print(f)
print(x)
