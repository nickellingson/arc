# use dict to store func and use decorator to choose func
REGISTRY = {}

def register(letter):
    def decorator(fn):
        REGISTRY[letter] = fn
        return fn
    return decorator

@register("a")
def print_a():
    print("a")

@register("b")
def print_b():
    print("b")

@register("c")
def print_c():
    print("c")

def call_letter(letter):
    fn = REGISTRY.get(letter)
    if fn:
        fn()
    else:
        print(f"No letter {letter} function")

print_a()
print_b()
print_c()

call_letter("a")
call_letter("d")
print()

# logging
def logger(fn):
    def deco(*args, **kwargs):
        print("before func")
        print("args", *args, **kwargs)
        try:
            result = fn(*args, **kwargs)
            return result
        except Exception as e:
            print(e)
            raise
        finally:
            print("after func")
    return deco

@logger
def func(a, b):
    return a + b

func(4, 5)