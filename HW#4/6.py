def fltn(ls):
    # flatten deep list
    if len(ls) == 0:
        return []
    elif type(ls[0]) == list:
        return fltn(ls[0]) + fltn(ls[1:])
    else:
        return [ls[0]] + fltn(ls[1:])

print("fltn([1,2,[3,4,[5,6]]]):", fltn([1,2,[3,4,[5,6]]]))
print("fltn([1,2,3]:", fltn([1,2,3]))
print("fltn([1,[2,3],4]:", fltn([1,[2,3],4]))
print("fltn([1,[2,[3,4],5],6]):", fltn([1,[2,[3,4],5],6]))
print("fltn([[1, [1, 1]], 1, [1, 1]]):", fltn([[1, [1, 1]], 1, [1, 1]]))
