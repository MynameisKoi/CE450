def amc(n):
    # Return the smallest amicable number greater than positive integer n.
    # If no amicable number exists, return None.
    def sum_factors(a):
        # Return a list of all factors of positive integer a.
        return sum([i for i in range(1,a) if a%i == 0])
    if n < 0:
        print("Error: n must be positive")
        return None
    else:
        if n < 220:
            # since the first amicable number is 220, we can skip all numbers < 220
            return 220
        else:
            for i in range(n+1, n**2):
                a = sum_factors(i)
                if sum_factors(a) == i and a != i:
                    return i
        return None

print("amc(5):", amc(5))
print("amc(220):", amc(220))
print("amc(284):", amc(284))
print("amc(5000):", amc(5000))
