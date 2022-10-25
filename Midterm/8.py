def is_plndrm(n):
    # use recursion to check whether input argument is palindrome
    if n < 10:
        return True
    else:
        if n % 10 == n // 10 ** (len(str(n)) - 1):
            return is_plndrm(n % 10 ** (len(str(n)) - 1) // 10)
        else:
            return False

print("is_plndrm(45654) = ", is_plndrm(45654)) # True
print("is_plndrm(42) = ", is_plndrm(42)) # False
print("is_plndrm(2019) = ", is_plndrm(2019)) # False
print("is_plndrm(10101) = ", is_plndrm(10101)) # True