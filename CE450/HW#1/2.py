def sum_odd(n):
    i = 0
    ans = 0
    while i <= n:
        if i % 2 != 0:
            ans += i
        i += 1
    return ans

print("sum_odd(6): ", sum_odd(6))
print("sum_odd(7): ", sum_odd(7))