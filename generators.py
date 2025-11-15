# generators

# lazy

def func_fib_lazy(n):
    p1, p2 = 1, 0
    temp = 0
    yield 0
    yield p1
    for i in range(n - 1):
        temp = p1
        p1 = p1 + p2
        p2 = temp
        yield p1


fib = func_fib_lazy(6)
print()
for seq_num in fib:
    print(seq_num, end=" ")
print()