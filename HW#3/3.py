from operator import add, neg
# import addition and negative transformation functions from operator module
def combine_funcs(op):
    def combined(f, g):
        # determine the combination functions from the argument (f and g)
        def val(x):
            # calculate the combined function at the given x
            return op(f(x), g(x))
            # return the result of the operation (an integer)
        return val
        # return the operation function to the combined functions (f and g)
    return combined
add_func = combine_funcs(add)
# add_func = combined(f, g) = add(f(x), g(x))
h = add_func(abs, neg)
# h = combined(abs, neg) = add(abs(x), neg(x))
print("h(-5) = ", h(-5))
# h(-5) = add(abs(-5), neg(-5)) = add(5, 5) = 10