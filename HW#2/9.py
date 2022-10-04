def A(n):
    if n <= 3: return n
    else:
        return A(n-1) + 2*A(n-2) + 3*A(n-3)

print("A(0): ", A(0))
print("A(1): ", A(1))
print("A(2): ", A(2))
print("A(3): ", A(3))
print("A(4): ", A(4))
print("A(5): ", A(5))
