def foo(f, n):
    # return the function that computes the nth application of f
    if f == "incr":
        return lambda x: x + n
    if f == "triple":
        return lambda x: x * (3 ** n)
    if f == "square":
        return lambda x: x ** (2 ** n)

# The three functions below are for single use application of f
def incr(x): return x + 1
def triple(x): return x * 3
def square(x): return x ** 2

print("incr(5): ", incr(5))
add3 = foo("incr", 3)
print("add3(5): ", add3(5))
print("foo(triple, 5)(1): ", foo("triple", 5)(1))
print("foo(square, 2)(5): ", foo("square", 2)(5))
print("foo(square, 4)(5): ", foo("square", 4)(5))
