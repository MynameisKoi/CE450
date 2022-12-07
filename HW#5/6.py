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

def change(lnk, u, v):
    if empty(lnk):
        return lnk
    # if lnk is not empty, change the linked list
    else:
        if lnk.first == u:
            lnk.first = v
        return link(lnk.first, change(lnk.rest, u, v))


l = link(1, link(2, link(3)))
print(l)
n = change(l, 3, 1)
print(n)
m = change(n, 1, 2)
print(m)
print(change(m, 5, 1))