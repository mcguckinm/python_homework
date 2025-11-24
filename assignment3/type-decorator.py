#Task 2

from sqlalchemy import func


def type_convertor(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

@type_convertor(str)
def return_int():
    return 5

@type_convertor(int)
def return_str():
    return "not a number"



#mainline code
y=return_int()
print (type(y).__name__)# should print str
try:
    y=return_str()
    print ("shouldn't get here")
except ValueError:
    print ("can't convert that string to an integer")
