def f1(n):
    def f2(m):
        return m + n
    return f2

n, m = int(input()), int(input())

f = f1(n)
print(f(m))