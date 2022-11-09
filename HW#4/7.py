def chk_elm(lst, n):
    # check if element exists in the deep list or not
    if len(lst) == 0:
        return False
    elif type(lst[0]) == list:
        return chk_elm(lst[0], n) or chk_elm(lst[1:], n)
    else:
        return lst[0] == n or chk_elm(lst[1:], n)

print("chk_elm([1,2,[3,4,[5,6]]], 5):", chk_elm([1,2,[3,4,[5,6]]], 5))
print("chk_elm([1,2,[3,4,[5,6]]], 7):", chk_elm([1,2,[3,4,[5,6]]], 7))
a = [[1,[2]],3,[[4],[5,[6]]]]
print("chk_elm(a, 6):", chk_elm(a, 6))