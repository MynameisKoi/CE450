def lrgst_factor(m):
    if m <= 1:
        print("Error: m must be greater than 1")
        return None
    else:
        for i in range(2,m):
            if m%i == 0:
                return int(m/i)
        return 1

print("lrgst_factor(15):", lrgst_factor(15))
print("lrgst_factor(80):", lrgst_factor(80))
print("lrgst_factor(100):", lrgst_factor(100))
print("lrgst_factor(7):", lrgst_factor(7))