def count(f):
    i = 1
    total = 0
    while True:
        if f(n, i):
            total += 1
        i += 1
    return total


def if_(i):
    while i <= n:
        return i
        i += 1

def count_factors():
    return lambda n, i: n % i == 0

def is_prime():
    return lambda n, i: count_factors(i) == 2

def count_cond(condition):
    return lambda n: count(lambda i: condition(n, i))

count_factors = count_cond(lambda n, i: n % i == 0)
is_prime = lambda n, i: count_factors(i) == 2
count_primes = count_cond(is_prime)
count_primes(16)


print_lambda = lambda z: print(z)
print_lambda
one_thousand = print_lambda(1000)
one_thousand

higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(2)(g)  # Which argument belongs to which function call?
higher_order_lambda(g)(2)