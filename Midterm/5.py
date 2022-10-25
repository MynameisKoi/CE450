pear = "ni"
def   apple(banana): # apple(lambda peach: 'ni' + peach)
                     # banana = lambda peach: 'ni' + peach
  def  plum(peach): # plum(lambda peach: 'ni' + peach)
    pear = lambda pear: peach(pear)
    # this line will take the argument 'ck' from the 'plum(banana)("ck") line'
    # peach('ck') => 'ni' + 'ck' => 'nick'
    return pear # pear = 'ck'
  return plum(banana)("ck")
  # plum(lambda peach: 'ni' + peach)('ck')

print(apple(lambda peach: pear + peach)) # peach('ck') => 'ni' + 'ck' => 'nick'
# return 'nick'