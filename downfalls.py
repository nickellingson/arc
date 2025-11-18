# Floating-point precision
0.1 + 0.2 == 0.3     # False
from decimal import Decimal; Decimal('0.1')+Decimal('0.2')==Decimal('0.3')  # True


# Mutable default args
def bad(x, acc=[]):           # BUG: shared list
    acc.append(x); return acc

def good(x, acc=None):
    if acc is None: acc=[]
    acc.append(x); return acc

# Late binding in lambdas
funcs = [lambda i=i: i for i in range(3)]  # capture at def time
[f() for f in funcs]  # [0,1,2]

# Shadowing built-ins
list = [1,2]   # BAD
del list       # or restart shell

# # BAD
# for x in a: 
#     if pred(x): a.remove(x)

# # GOOD
# a = [x for x in a if not pred(x)]
# # OR iterate over copy:
# for x in a[:]: ...