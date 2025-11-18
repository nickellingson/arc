import heapq
import bisect
import collections
import os
import sys
import math
import random
import datetime
import dis
import site



print(sys.base_prefix)
print(sys.prefix)



# how returns work
def f(x): 
    y = x + 1
    return y

dis.dis(f)
# ... LOAD_FAST x; LOAD_CONST 1; BINARY_OP [+]; STORE_FAST y
# LOAD_FAST y
# RETURN_VALUE