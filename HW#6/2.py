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

def lst(t):
    # Return a list of the labels in Tree t
        if t.is_leaf():
            return [t.label]
        # if t is not empty, return the list of the labels in Tree t
        else:
            return [t.label] + lst(t.branches[0]) + lst(t.branches[1])

def ave(t):
    # Return the average of the labels in Tree t
    # t: Tree
    # return: average
    # pass empty (null) values
    if t.is_leaf():
        return t.label
    # if t is not empty, return the average of the labels in Tree t
    else:
        return sum(lst(t))/len(lst(t))

t = Tree(11, [Tree(12), Tree(13, [Tree(14),Tree(15)])] )
# print(lst(t)) => the list of the tree will be [11, 12, 13, 14, 15]
print(ave(t))