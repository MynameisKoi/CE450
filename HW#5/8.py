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

def insrt(l, elm, ind):
    # insert elm into linked list l at index ind
    # l: linked list
    # elm: element
    # ind: index
    # return: linked list
    # pass empty (null) values
    if empty(l):
        return link(elm)
    # if ind is 0, insert elm at the beginning of the linked list
    elif ind == 0:
        return link(elm, l)
    # if ind is not 0, insert elm at the index ind
    else:
        return link(l.first, insrt(l.rest, elm, ind-1))

l = link(11, link(12, link(13)))
n = insrt(l, 2021, 1)
print(n)
m = insrt(n, 2022, 20)
print(m)
