def   horn(hood):
  horn = hood # in this case, horn = hood = lambda horn: horn(2)
  def  hood (horn):
    # first time called:
    # the line will change 'hood' from a value to a function name
    # now hood != horn of the line above

    # second time called:
    # hood(horn) = hood(2) => horn = 2
    return horn # return 2
  return horn(hood)
  # the line will call back to the lambda horn of the code line below
hood = lambda horn: horn(2)
print(horn(hood))
# the function 'horn' takes an argument 'hood'
# which is lambda horn: horn(2)
# this will call the 'horn(hood)' function
# horn(lambda horn: horn(2))