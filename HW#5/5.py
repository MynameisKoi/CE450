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

def sum_lnk(lnk, g):
    # apply function g to each element in the linked list and return the sum
    if empty(lnk):
        return 0
    else:
        return g(lnk.first) + sum_lnk(lnk.rest, g)
dbl = lambda y: y*2
sqr = lambda x: x*x

lnk1 = link(1,link(2,link(3,link(4))))
print(sum_lnk(lnk1, sqr))

lnk2 = link(3, link(5, link(4, link(6))))
print(sum_lnk(lnk2, dbl))

lnk3 = link(3, link(3, link(3)))
print(sum_lnk(lnk3, sqr))