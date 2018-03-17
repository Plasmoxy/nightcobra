
def decor(f):
    def wrap(x):
        print('===')
        print('' = ' + f(x))
        print('===')
    return wrap

@decor
def p(x):
    return x**2

p(2)
