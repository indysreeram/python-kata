message = ''' The property of certain operations in mathematics and computer
science,that can be appied multiple times without changing the results beyond
the initial application.'''
print(message)

def add_ten(num):
    return num+10
# f(f(x)) =f(x)
# f(f(10)) =30 | f(10) =20 hence not idempotent
print (add_ten(10))
print (add_ten(add_ten(10)))
# so the above is not idempotent


# f(f(x)) =f(x)
# The result is the same which is 10
print(abs(-10))
print(abs(abs(-10)))
# so the above is idempotent

a=10 # This is idempotent
a=10 # This is idempotent
a=10 # This is idempotent
a=10 # This is idempotent

print(a)
#HTTP METHODS
#GET  -> This idempotent
#PUT -> This idempotent and in  this is used to update a resource.
#POST -> This is not idempotent and used to change data or resource.
#DELETE -> This idempotent because deleting multiple times the same result as
            #resource is deleted.
