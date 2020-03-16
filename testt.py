from math import sqrt
def square_root(num) :
    if num >= 0:
        print(num ** 0.5)
    else :
        print('Value - input- has no integer square root')

def square_root_new(num) :
    if num >= 0:
        print('Value - input- has integer square root', round(sqrt(num),3))
    else :
        print('Value - input- has no integer square root')

def plus(i1,i2):
    print(i1 + i2)
    return(i1 + i2)
def minus(i1,i2):
    print(i1 - i2)
    return(i1 - i2)
def multiply(i1,i2):
    print(i1 * i2)
    return(i1 * i2)
def divide(i1,i2):
    if i2 == 0:
        print("Can't divide by zero.")
        return 0
    print(i1 / i2)
    return(i1 / i2)
def calculator(x,y,operation):
    if operation == plus:
        t = plus(x,y)
    else:
        if operation == minus:
            t = minus(x, y)
        else:
            if operation == multiply:
                t = multiply(x, y)
            else:
                t = divide(x, y)
    if t > 0:
        print('the result is possitive')
    else:
        if t == 0:
            print('the result is zero')
        else:
            print('the result is negative')
calculator(2,2,plus)

my_list = [[10, 10], [100, 100], [500, 500, 1000]]
for val in my_list:
    new_list = [i for i in val if i > 10]
print(new_list)
