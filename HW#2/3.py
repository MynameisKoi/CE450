def cnt_primes(n):
    if n == 0: return 0
    # check if a number is prime
    def is_prime(n):
        if n == 1: return False
        for i in range(2, n):
            if n % i == 0: return False
        return True
    # count the number of primes
    if is_prime(n): return 1 + cnt_primes(n-1)
    else: return cnt_primes(n-1)

print("cnt_primes(6): ", cnt_primes(6))
print("cnt_primes(10): ", cnt_primes(10))
print("cnt_primes(20): ", cnt_primes(20))