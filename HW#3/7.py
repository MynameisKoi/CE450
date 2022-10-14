def cyc(g1,g2,g3):
    def y(n):
        if n == 0:
            return lambda x: x
        elif n == 1:
            return lambda x: g1(x)
        elif n == 2:
            return lambda x: g2(g1(x))
        elif n == 3:
            return lambda x: g3(g2(g1(x)))
        else:
            return lambda x: y(n-3)(g3(g2(g1(x))))
    return y

def add_one(x):
    return x+1
def times_two(x):
    return x*2
def add_three(x):
    return x+3

my_cyc = cyc(add_one, times_two, add_three)
h = my_cyc(0)
print("h(5) = my_cyc(0)(5) =", h(5))
h = my_cyc(2)
print("h(1) = my_cyc(2)(1) =", h(1))
h = my_cyc(3)
print("h(2) = my_cyc(3)(2) =", h(2))
h = my_cyc(4)
print("h(2) = my_cyc(4)(2) =", h(2))
h = my_cyc(6)
print("h(1) = my_cyc(6)(1) =", h(1))
h = my_cyc(10)
print("h(2) = my_cyc(10)(2) =", h(2))