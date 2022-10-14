def smth(g, dx):
    return lambda x: (g(x-dx) + g(x) + g(x+dx))/3

square = lambda x: x**2
cube = lambda x: x**3
triple = lambda x: 3*x
increment = lambda x: x+1

print("round(smth(square, 1)(0), 3)):", round(smth(square, 1)(0), 3))
print("round(smth(cube, 2)(2), 3)):", round(smth(cube, 2)(2), 3))
print("round(smth(triple, 3)(1), 3)):", round(smth(triple, 3)(1), 3))
print("round(smth(increment, 5)(7), 3)):", round(smth(increment, 5)(7), 3))