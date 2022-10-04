def fancy_printing(n):
# Assume that the specified range is 0 to 30
    for i in range(0, 31):
        if i == 0: # Print 0
            print(i)
            continue
        if n % i == 0:
            print("Buzz!")
        else:
            print(i)

print("fancy_printing(3): ")
fancy_printing(3)
print("fancy_printing(5): ")
fancy_printing(5)
print("fancy_printing(20): ")
fancy_printing(20)
