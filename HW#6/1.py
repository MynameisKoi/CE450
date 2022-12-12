class Tree:
  def __init__(self, label, branches=[]):
    self.label = label
    for branch in branches:
      assert isinstance(branch, Tree)
    self.branches = list(branches)
  def __repr__(self):
    if self.branches:
      return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
    else:
      return 'Tree({0})'.format(repr(self.label))
  def __str__(self):
    return '\n'.join(self.indented())

  def indented(self):
    lines = []
    for b in self.branches:
      for line in b.indented():
        lines.append('  ' + line)
    return [str(self.label)] + lines

  def is_leaf(self):
    return not self.branches

def has_itm(t, e):
  # Return True if a Tree t contains the value e
    # t: Tree
    # e: element
    # return: True or False
    if t.is_leaf():
        return False
    # if e is in the Tree t, return True
    elif t.label == e:
        return True
    # if e is not in the Tree t, return False
    else:
        return has_itm(t.branches[0], e) or has_itm(t.branches[1], e)

print(has_itm (Tree(11, [Tree(12), Tree(13, [Tree(14),Tree(15)])] ),  11))
print(has_itm (Tree(11, [Tree(12), Tree(13, [Tree(14),Tree(15)])] ),  16))