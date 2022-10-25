import math
def nrst_two(x):
    if x <= 0:
        return 0
    else:
        a = math.log2(x)
        up = math.ceil(a)
        down = math.floor(a)
        go_up = 2**up
        go_down = 2**down
        if go_up - x > x - go_down:
            return go_down
        else:
            return go_up

print("nrst_two(8) = ", nrst_two(8)) # 8
print("nrst_two(11.5) = ", nrst_two(11.5)) # 8, since it is closer to 2**3 than 2**4
print("nrst_two(14) = ", nrst_two(14)) # 16
print("nrst_two(2019) = ", nrst_two(2019)) # 2048
print("nrst_two(0.1) = ", nrst_two(0.1)) # 0.125
print("nrst_two(0.75) = ", nrst_two(0.75)) # 1
print("nrst_two(1.5) = ", nrst_two(1.5)) # 2