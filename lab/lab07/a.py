x = 5

def f(x):
    def g(s):
        def h(h):
            nonlocal x
            x = x + h
            return x
        nonlocal x
        x = x + x
        return h
    print(x)
    return g

t = f(7)(8)(9)