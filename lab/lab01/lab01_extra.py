"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    total = 1
    while k >= 1:
        total, n = total * n, n -1
        k = k -1
    return total




def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    def pow_count(n):
        return len(str(n))-1
    def pow_a(n):
        return pow(10, pow_count(n))
    def digit_count(n):
        return n // pow(10, pow_count(n))
    while n > 1:
        i = digit_count(n)
        a = pow_count(n)
        n = n - digit_count(n) * pow_a(n)
        j = digit_count(n)
        b = pow_count(n)
        k = i * j
        l = a - b
        if k == 64 and l == 1:
            return True
    else:
        return False