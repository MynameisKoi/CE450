def verify_add(m, ls):
    # return true if addition of any two different elements in ls is m
    # return false otherwise
    for i in range(len(ls)):
        if m - ls[i] in ls and m - ls[i] != ls[i]:
            return True
    return False

print(verify_add(100, [1,2,3,4,5]))
print(verify_add (7, [1, 2, 3, 4, 2]))
print(verify_add(10, [5,5]))
print(verify_add(151, range(0, 200000, 3)))
print(verify_add(50004, range(0, 200000, 4)))