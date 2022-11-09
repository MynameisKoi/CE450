def sym(l):
    # check whether the list is symmetric recursively
    if len(l) == 0 or len(l) == 1:
        return True
    elif len(l) == 2:
        return l[0] == l[1]
    else:
        return l[0] == l[-1] and sym(l[1:-1])

print("sym([1,2,3,2,1]):", sym([1,2,3,2,1]))
print("sym([1,2,3,3,2,1]):", sym([1,2,3,3,2,1]))
print("sym([]):", sym([]))
print("sym([1]):", sym([1]))
print("sym([1,4,5,1]):", sym([1,4,5,1]))
print("sym([1,4,4,1]):", sym([1,4,4,1]))
print("sym(['l','o','l']):", sym(['l','o','l']))
