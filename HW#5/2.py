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
        else:
            rest_repr = ''
        return 'link(' + repr(self.first) + rest_repr + ')'

def empty(s):
    return s is link.empty

def prnt_lnk(s):
        string = '<'
        while s.rest is not link.empty:
            string += str(s.first) + ' '
            s = s.rest
        return string + str(s.first) + '>'

a = link(1,link(2,link(3,link(4))))
print(prnt_lnk(a))


