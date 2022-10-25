woo = 6
def  much(woo):
  if much == woo:
    # first order of the function:
    # since the value of the argument 'woo' is the same as the function name 'much'
    # the condition is true and the following code is executed

    # second order of the function:
    # the function is called again, but this time the argument 'woo' is the value of the local variable 'woo'
    # which is 6
    # the condition is false
    such = lambda woo: 5
    # the 'such' function will take the second 'woo' value in 'much(much(much))(woo)'
    # however, whatever the argument is, the function will always return 5
    def woo():
    # this will change 'woo' from a value to a function name
      return such
    return  woo
    # the function will return itself
  such = lambda woo: 4
  # in the second order of the function, the 'such' function will take the value of the local variable 'woo'
  # which is 6, however, whatever the argument is, the function will always return 4
  # such = 4 (local variable of the second order 'much' function)
  return woo()
  # when this line is executed, it goes back to the 'def woo():' line
  # it will return the such function (whose parent function is the first order of 'much')
  # thus, it will return 5

woo = much(much(much))(woo)
# this assign 'woo' value to the value of 'much' function
print(woo)