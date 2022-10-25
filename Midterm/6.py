x = "x"
g = x # g = x = "x"
def x(x): # x becomes the name of function, x != "x"
  g = "h" # local variable g = "h"
  if x == g: # this false because g = "h" and x != "x"
    return x + "i"
  x = lambda x: x(g) # x = lambda x: x("h")
                     # now x does not point to the function name 'x' anymore
                     # this 'x' has the parent function which is the function 'x' above
  return lambda g: x(g)
  #

x = x(x)(x)
# x(x) = x(lambda x: x("h")) = lambda g: x(g)
# x(x)(x) = x(lambda x: x("h"))(x) = x("h")

# on the second call of x("h"), the condition is true since argument x = "h" and g = "h"
# thus, the function will return "hi"
print(x)