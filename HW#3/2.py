def adder(f1, f2):
    return lambda x: f1(x) + f2(x)

def square(n): return n**2
def identity(n): return n

a1 = adder(identity, square)
print("a1(4) = ", a1(4))
a2 = adder(a1, identity)
print("a2(4) = ", a2(4))
print("a2(5) = ", a2(5))
a3 = adder(a1, a2)
print("a3(4) = ", a3(4))