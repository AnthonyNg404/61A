def square(x):
    return x * x

def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def inverse(f, i):
    return search(lambda x: f(x) == i)

inverse(square, 16)

def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie

chocolate = cake()
chocolate
chocolate()
more_chocolate, more_cake = chocolate(), cake
more_chocolate