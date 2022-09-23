def uniq_digits(x):
    # return the number of unique digits in positive integer x
    if x < 0:
        print("Error: x must be positive")
        return None
    else:
        return len(set(str(x)))

print("uniq_digits(8675309):", uniq_digits(8675309))
print("uniq_digits(1313131):", uniq_digits(1313131))
print("uniq_digits(13173131):", uniq_digits(13173131))
print("uniq_digits(10000):", uniq_digits(10000))
print("uniq_digits(101):", uniq_digits(101))
print("uniq_digits(10):", uniq_digits(10))