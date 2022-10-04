def op(a,b,c):
    # computes a*b + c using only recursion
    if a == 0:
        return c
    if a > 0:
        return op(a-1,b,c+b)
    if a < 0:
        return op(a+1,b,c-b)

print("op(2,3,4): ", op(2,3,4))
print("op(0,3,2): ", op(0,3,2))
print("op(3,0,2): ", op(3,0,2))
print("op(-10,3,2): ", op(-10,3,2))
print("op(-5,-3,2): ", op(-5,-3,2))
