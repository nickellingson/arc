# What comes to mind
# __init__ → constructor
# __new__ → object creation before init
# __str__ → human string
# __repr__ → debug string
# __len__, __getitem__, __iter__ → container protocol
# __enter__, __exit__ → context manager
# __call__ → object behaves like function
# __slots__
# __eq__
# __defaults__

# list more dunder/magic methods
print("STRINGS")
print(dir(str))
print("INTEGERS")
print(dir(int))
print("TYPE")
print(dir(type))
print("CLASS METHOD")
print(dir(classmethod))
print()
# ....

# __init__ -> invoked without a call when class instance is created (constructor)
class Hello:

    def __init__(self, name):
        self.name = name
    
    def print_greeting(self):
        print(f"Hello {self.name}")
class_instance_hello = Hello("Bob")
class_instance_hello.print_greeting()
print()

# __repr__ defines an object is presented as a string (string representation of an object)
greeting = "hello"
num = 2
print(greeting)
print(greeting.__repr__())
print(num.__repr__())
print(type(num)) # <class 'int'>
print(type(num.__repr__())) # <class 'str'>
print()

# __eq__ equality operator ==
a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a.__eq__(b))
print(a is b)
print()