def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result

print("if_function(True, 2, 3): " , if_function(True, 2, 3))
print("if_function(False, 2, 3): ", if_function(False, 2, 3))
print("if_function(3 == 2, 3+2, 3-2): ", if_function(3 == 2, 3+2, 3-2))
print("if_function(3 > 2, 3+2, 3-2): ", if_function(3 > 2, 3+2, 3-2))
