class link:
    empty = ()
    def __init__(self, first, rest=empty):
   # isinstance(a, A): whether "a" is one of instances of A
        assert rest is link.empty or isinstance(rest, link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        elif self.rest is link.empty:
            rest_repr = ',[]'
        else:
            rest_repr = ''
        return '[' + repr(self.first) + rest_repr + ']'

def empty(s):
    return s is link.empty

def first(s): # first function for class link
    assert s is not link.empty
    return s.first

def rest(s): # rest function for class link
    assert s is not link.empty
    return s.rest

def apnd(lnk, m):
    # add the element m to the end of the linked list
    # lnk: linked list
    # m: element to be added
    # return: linked list with m added to the end
    # pass empty (null) values
    if empty(lnk):
        return link(m)
    # if lnk is not empty, add m to the end of the linked list
    else:
        # create a new linked list
        new_lnk = link(lnk.first)
        # while lnk is not empty, add m to the end of the linked list
        while lnk.rest is not link.empty:
            # add the first element of lnk to the new linked list
            new_lnk = link(lnk.rest.first, new_lnk)
            # move to the next element of lnk
            lnk = lnk.rest
        # add m to the end of the linked list
        new_lnk = link(m, new_lnk)

        # reverse the new_lnk to get the final linked list
        result_lnk = link(new_lnk.first)
        while new_lnk.rest is not link.empty:
            result_lnk = link(new_lnk.rest.first, result_lnk)
            new_lnk = new_lnk.rest
        return result_lnk

l = link(1, link(2, link(3)))
print(l)
n = apnd(l, 4)
print(n)

print(first(rest(rest(rest(n))))) # 4