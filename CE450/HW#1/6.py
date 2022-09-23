def pfct_num(m):
    a = 1
    while m > 0:
        m -= a
        a += 1
    return m == 0

print("pfct_num(6):", pfct_num(6))
print("pfct_num(8):", pfct_num(8))
print("pfct_num(28):", pfct_num(28))