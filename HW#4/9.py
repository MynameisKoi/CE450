from operator import add, sub, mul

def fld(lst, g, m):
    # if lst has no element, return m
    if len(lst) == 0:
        return m
    # if g = sub, subtract m by each element in lst
    if g == sub:
        # recursive
        return fld(lst[1:], g, g(m, lst[0]))
    return g(lst[0], fld(lst[1:], g, m))


s = [3,2,1]
print("fld(s,sub,0):", fld(s,sub,0)) # -6
print("fld(s,add,0):", fld(s,add,0)) # 6
print("fld(s,mul,1):", fld(s,mul,1)) # 6
print("fld([],sub,100):", fld([],sub,100)) # 100