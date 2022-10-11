def has_seven(k, target):
    # check if a number k has the target digit by recursion
    if k == 0:
        return False
    elif k % 10 == target:
        return True
    else:
        return has_seven(k // 10, target)

print("has_seven(3,7): ", has_seven(3,7))
print("has_seven(7,7): ", has_seven(7,7))
print("has_seven(2734,7): ", has_seven(2734,7))
print("has_seven(2634,7): ", has_seven(2634,7))
print("has_seven(734,7): ", has_seven(734,7))
print("")

# ----------------------------------------------------------------#
# ------------------GENERAL FORM OF FUNCTIONS --------------------#
def has_digit(k, target):
    # check if a number k has the target digit by recursion
    if k == 0:
        return False
    elif k % 10 == target:
        return True
    else:
        return has_digit(k // 10, target)

# check for a number k has digit 7
print("has_digit(7,7): ", has_digit(7,7))
print("has_digit(2734,7): ", has_digit(2734,7))
print("has_digit(2634,7): ", has_digit(2634,7))
print(" ")
# check for a number k has digit 2
print("has_digit(2734,2): ", has_digit(2734,2))
print("has_digit(2634,2): ", has_digit(2634,2))
print("has_digit(734,2): ", has_digit(734,2))