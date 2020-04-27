print('Main module imported!!!')

def add(x, y):
    return x + y

def mutiply(x,y):
    return x * y

def inc(x):
    return x + 1

def divide(x,y):
    if y > 0:
        return x/y 
    else:
        raise ZeroDivisionError("Division by zero not allowed!!!") 

