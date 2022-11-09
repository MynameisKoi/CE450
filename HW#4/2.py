def rm_all(elem, lst):
    # remove all instances of element from a list
    while elem in lst:
        lst.remove(elem)
    return lst

x = [3,1,2,1,5,1,1,7]
print("rm_all(1, x):", rm_all(1, x))

y = [3,2,3,5,5,6,8,1,3]
print("rm_all(3, y):", rm_all(3, y))
print("rm_all(5, y):", rm_all(5, y))