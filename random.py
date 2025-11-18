import copy

# shallow vs deep copy
a = [[1],[2]]
b = copy.copy(a)       # shallow: inner lists shared
c = copy.deepcopy(a)   # deep: inner lists cloned

a[0].append(99)
b[0]    # [1, 99]  (shared)
c[0]    # [1]      (independent)


# Reference semantics (no copying)
# Python returns references to objects; it does not copy the data. The refcount is adjusted.
# Returning a big list does not duplicate it; mutability rules still apply.

def g(L): return L
A = [1,2]
B = g(A)
print(A is B)  # True

a = 10
b = 10

print(a is b)
print(a = b)

# Implicit None, tuple packing, multiple values
# return with no expression → returns None.
# return a, b actually returns a tuple (tuple packing).

def h(): pass
h() is None  # True

def t(): return 1, 2
t()          # (1, 2)


def w():
    with open("x.txt","w") as f:
        return 42          # f.__exit__ runs before the function returns

def tricky():
    try:
        return "try"
    finally:
        return "finally"   # overrides -> returns "finally"
    


def gen():
    if True:
        return 99          # becomes StopIteration(99)
    yield 1

def outer():
    v = yield from gen()
    return v               # v == 99 here

it = outer()
try:
    next(it)
except StopIteration as e:
    e.value  # 99


import asyncio
# async def, return resolves the coroutine’s result.
async def a(): return 7
async def b(): 
    r = await a()  # gets 7
    return r


def order():
    try:
        try:
            return 1
        finally:
            print("inner")
    finally:
        print("outer")
# prints: inner \n outer


import numpy as np
def view(a): return a[::2]  # shares memory
def copy(a): return a[::2].copy()


def f():
    try:
        return "try"
    finally:
        return "finally"
assert f() == "finally"



def g():
    return 10
def G():
    v = yield from g()  # actually not a generator; g returns 10 immediately
    return v            # unreachable; G has no yield -> not a generator

def h():
    yield 1
    return 10
def H():
    r = yield from h()
    return r

it = H()
next(it)            # yields 1 from h
try:
    next(it)
except StopIteration as e:
    assert e.value == 10


import dis
dis.dis(lambda x: x+1)
# ... BINARY_OP [+]; RETURN_VALUE



def id_echo(x): return x
a = object()
assert id_echo(a) is a

# fstring eval feature
# f"{x+1=}"



def stream_lines(path):
    with open(path, 'rt') as f:
        for line in f:       # buffered iteration
            yield line.rstrip('\n')


# eval():
# Purpose: Evaluates a single Python expression.
# Return Value: Returns the result of the evaluated expression.

result = eval("2 + 3 * 4")
print(result) # Output: 14

# exec():
# Purpose: Executes a block of Python statements.
# Return Value: Always returns None. Its purpose is to perform actions (like variable assignments, function definitions, etc.), not to produce a single return value.
code_block = """
x = 10
y = 20
z = x + y
print(z)
"""
exec(code_block) # Output: 30

# threadpoolexecutor vs processpoolexecuter
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# def io_task(u): ...
# def cpu_task(n): ...

# # I/O bound (threads OK; GIL mostly idle on I/O)
# with ThreadPoolExecutor(32) as ex: ex.map(io_task, urls)

# # CPU bound (processes bypass GIL, real parallelism)
# with ProcessPoolExecutor() as ex: ex.map(cpu_task, nums)