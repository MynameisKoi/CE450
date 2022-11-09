def add_many(x, elem, lst):
    a = lst.count(x)
    for i in range(a):
        lst.append(elem)
    return lst

lst = [1,2,4,2,1]
print("add_many(2,5,lst):", add_many(2,5,lst))
lst_2 = [1,3,3,5,8,3]
print("add_many(3,7,lst_2):", add_many(3,7,lst_2))
