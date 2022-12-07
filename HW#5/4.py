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

def srt(link):
    # if the linked list is sorted, return true
    if link.rest is link.empty:
        return True
    # if the linked list is not sorted, return false
    elif link.first > link.rest.first:
        return False
    # if the linked list is not empty, return srt(link.rest)
    else:
        return srt(link.rest)

lnk1 = link(1,link(2,link(3,link(4))))
print(srt(lnk1))

lnk2 = link(1, link(3, link(2, link(4, link(5)))))
print(srt(lnk2))

lnk3 = link(3, link(3, link(3)))
print(srt(lnk3))