def same_ord(a, b):
    #check if the number of digits from two positive input parameters is the same or not.
    #return True if the number of digits is the same, otherwise return False.
    if a < 0 or b < 0:
        print("Error: a and b must be positive")
        return None
    else:
        return len(str(a)) == len(str(b))

print("same_ord(5, 3):", same_ord(5, 3))
print("same_ord(50, 70):", same_ord(50, 70))
print("same_ord(50, 100):", same_ord(50, 100))
print("same_ord(1000, 10000):", same_ord(1000, 10000))