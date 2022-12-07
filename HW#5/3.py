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

def rvrs_lnk(s):
    # Return a reversed linked list
    # s: linked list
    # return: reversed linked list
    # pass empty (null) values
    if empty(s):
        return s
    # if s is not empty, reverse the linked list
    else:
        # create a new linked list
        new_lnk = link(s.first)
        # while s is not empty, reverse the linked list
        while s.rest is not link.empty:
            # add the first element of s to the new linked list
            new_lnk = link(s.rest.first, new_lnk)
            # move to the next element of s
            s = s.rest
        return new_lnk

a = link(1,link(2,link(3,link(4))))
print(rvrs_lnk(a))


