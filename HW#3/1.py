def abndnt(n):
    sum = 1
    for i in range(1, n//2):
        if n % i == 0:
            print(i, "*", n//i)
            if i != 1:
                sum += i + n//i
    if sum > n:
        return True
    else:
        return False

print("abndnt(12) = ", abndnt(12))
print("abndnt(14) = ", abndnt(14))
print("abndnt(16) = ", abndnt(16))
print("abndnt(20) = ", abndnt(20))
print("abndnt(22) = ", abndnt(22))
print("abndnt(24) = ", abndnt(24))
