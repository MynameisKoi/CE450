def trc1(g):
    def f(args):
        print('Calling', g.__name__, 'on argument', args)
        return g(args)
    return f

@trc1
def sqr(x):
    return x*x

@trc1
def sum_sqr(n):
    return sum(sqr(x) for x in range(n+1))

print(sqr(3))
print(sum_sqr(3))