
def num_sevens(n):
    if n == 0:
        return 0
    if n % 10 == 7:
        return num_sevens(n // 10) + 1
    else:
        return num_sevens(n // 10)

def count_reverse(s):
    if s == 0:
        return 0
    if num_sevens(s) > 0 or s % 7 == 0:
        return count_reverse(s - 1) + 1
    else:
        return count_reverse(s - 1)

for i in range(0,5):
    print(i)

x = []
for i in range(0, 9) :
    x[0] = i

print(x)

