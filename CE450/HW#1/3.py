def foo(a,b,c,d):
    num = [a,b,c,d]
    x = min(num)
    num.remove(x)
    y = min(num)
    return x**2 + y**2

print("foo(1,2,3,4): ", foo(1,2,3,4))
print("foo(-3,1,5,6): ", foo(-3,1,5,6))