def deep_rvrs(tup):
    # reverse tuple with possible tuple elements
    # return reversed tuple
    if len(tup) == 0:
        return tup
    elif type(tup[0]) == tuple:
        return deep_rvrs(tup[1:]) + (deep_rvrs(tup[0]),)
    return deep_rvrs(tup[1:]) + (tup[0],)

a = (11,12,13,14)
print(deep_rvrs(a))
tpl = (11,(12,(13,113),14),15)
print(deep_rvrs(tpl))