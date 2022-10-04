def intscts(f, x):
    # Returns a function that returns whether f intersects function g at x
    def square(x): return x ** 2
    def triple(x): return x * 3
    def identity(x): return x
    def increment(x): return x + 1
    def g(y):
        if y == "square":
            return square(x)
        if y == "triple":
            return triple(x)
        if y == "identity":
            return identity(x)
        if y == "increment":
            return increment(x)
    if f == "square":
        return lambda y: g(y) == square(x)
    if f == "triple":
        return lambda y: g(y) == triple(x)
    if f == "identity":
        return lambda y: g(y) == identity(x)
    if f == "increment":
        return lambda y: g(y) == increment(x)

at3 = intscts("square", 3)
print("at3(triple): ", at3("triple"))
print("at3(increment): ", at3("increment"))

at1 = intscts("identity", 1)
print("at1(square): ", at1("square"))
print("at1(triple): ", at1("triple"))