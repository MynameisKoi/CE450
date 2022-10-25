def has_subls(ls, subls):
    # return if the elements of subls appear in ls in any order
    # return True if subls is empty
    if subls == []:
        return True
    else:
        if subls[0] in ls:
            return has_subls(ls, subls[1:])
        else:
            return False

print("has_subls([], []) = ", has_subls([], [])) # True
print("has_subls([3, 3, 2, 1], []) = ", has_subls([3, 3, 2, 1], [])) # True
print("has_subls([], [3, 3, 2, 1]) = ", has_subls([], [3, 3, 2, 1])) # False
print("has_subls([3, 3, 2, 1], [3, 2, 1]) = ", has_subls([3, 3, 2, 1], [3, 2, 1])) # True
print("has_subls([3, 2, 1], [3, 2, 1]) = ", has_subls([3, 2, 1], [3, 2, 1])) # True
