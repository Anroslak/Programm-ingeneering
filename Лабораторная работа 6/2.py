def f1(n):
    return n**3

def f2(n):
    return n*2

n = int(input())
f = f1(f2(n))
print(f)