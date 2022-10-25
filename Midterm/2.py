def  Ton(now):
    then = 42
    def no(know): # in the case below, no(4) is executed
                  # know = 4
        no = then # no = 42, however this is a local variable
        return  know * now(know) # this equals to 4 * now(know)
                                 # and now = lambda oh: oh * 4
                                 # so now(4) = 4 * 4 = 16
        # know * now(know) = 4 * 16 = 64
    return no # return the result of 'no' function, not the value of local no variable
              # 64

then, no = 7,4 # then = 7, no = 4
now = lambda oh: oh * no # now = lambda oh: oh * 4
ok = Ton(now)(no) # ok = Ton(lambda oh: oh * 4)(4)
print(ok)