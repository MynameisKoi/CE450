def mk_wd(balance):
    def f(x):
        nonlocal balance
        if x > balance:
            return 'Insufficient funds'
        balance -= x
        return balance
    return f

rem = mk_wd(100)
print("rem(10): ", rem(10))
print("rem(20): ", rem(20))
print("rem(100): ", rem(100))
