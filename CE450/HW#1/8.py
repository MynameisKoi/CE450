def double_5(n):
    # return True if n has two fives in a row
    if n < 0:
        print("Error: n must be positive")
        return None
    else:
        return "55" in str(n)

print("double_5(5):", double_5(5))
print("double_5(55):", double_5(55))
print("double_5(550055):", double_5(550055))
print("double_5(12345):", double_5(12345))
print("double_5(505050):", double_5(505050))