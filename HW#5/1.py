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

    def __str__(self):
        string = '<'
        while self.rest is not link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'

def empty(s):
    return s is link.empty

def cntn_link(s, elm):
    # Return True if elm is in the linked list s
    # s: linked list
    # elm: element
    # return: True or False
    # pass empty (null) values
    if empty(s):
        return False
    # if elm is in the linked list s, return True
    elif s.first == elm:
        return True
    # if elm is not in the linked list s, return False
    else:
        return cntn_link(s.rest, elm)


a = cntn_link(link(1, link(2, link(3))), 1)
print(a)

b = cntn_link(link(1, link(2, link(3))), 4)
print(b)
