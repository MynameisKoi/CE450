def cal(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * cal(n-2)

print("cal(4): ", cal(4))
print("cal(5): ", cal(5))
print("cal(8): ", cal(8))
print("cal(9): ", cal(9))