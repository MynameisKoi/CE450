def df(x,y,z):
    # takes three integers x, y, and z. It returns whether subtracting one of these numbers from another gives the third.
    if x+y == z:
        return True
    elif x+z == y:
        return True
    elif y+z == x:
        return True
    else:
        return False

print("df(5,3,2):", df(5,3,2))
print("df(2,3,5):", df(2,3,5))
print("df(2,5,3):", df(2,5,3))
print("df(-2,3,5):", df(-2,3,5))
print("df(-5,-3,-2):", df(-5,-3,-2))
print("df(-2,3,-5):", df(-2,3,-5))
print("df(2,3,-5):", df(2,3,-5))
print("df(10,6,4):", df(10,6,4))
print("df(10,6,3):", df(10,6,3))