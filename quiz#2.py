from math import sqrt
def is_sqrt(seq):
    ans = []
    for i in seq:
        if sqrt(i) == int(sqrt(i)):
            ans.append(i)
    return ans

seq = [49, 8, 2, 1, 102]
print("seq = [49, 8, 2, 1, 102]:", is_sqrt(seq))

seq = [500, 30]
print("seq = [500, 30]:", is_sqrt(seq))

seq = [64, 24, 27, 100, 81, 25]
print("seq = [64, 24, 27, 100, 81, 25]:", is_sqrt(seq))
