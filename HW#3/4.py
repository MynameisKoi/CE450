def intsct(f, x):
    def g(y): return y(x)
    return lambda y: g(y) == f(x)

def triple(x): return x * 3
def square(x): return x ** 2
def identity(x): return x
def increment(x): return x + 1

at_three = intsct(square, 3)
print("at_three(triple): ", at_three(triple))
print("at_three(increment): ", at_three(increment))
at_one = intsct(identity, 1)
print("at_one(square): ", at_one(square))
print("at_one(triple): ", at_one(triple))
