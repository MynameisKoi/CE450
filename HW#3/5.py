def f():
    def g():
        def h(x):
            def i():
                return x
            return i
        return h
    return g

print("f()()(3)():", f()()(3)())
