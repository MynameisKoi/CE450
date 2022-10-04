def checking(x):
    # return True if the (base) digits of x > 0 are in non-decreasing order, and False otherwise
    if x < 10: return True
    if x % 10 < (x // 10) % 10: return False
    return checking(x // 10)

print("checking(5): ", checking(5))
print("checking(11): ", checking(11))
print("checking(127): ", checking(127))
print("checking(1357): ", checking(1357))
print("checking(21): ", checking(21))
result = checking(1375)
print(result)