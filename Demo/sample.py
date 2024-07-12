
def func(x):
    return x+1


def add (a,b):
    return a+b

def calculatorAdd (a,b):
    return a+b

def calculatorSub (a, b):
    return a-b

def calculatorMultiply (a, b):
    return a*b

def calculatorDevide (a, b):
    if(b==0):
        raise ValueError("value of b=0 is not allowed")
    return a/b