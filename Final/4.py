class Fibonacci():
    def __init__(self):
        self.val = 0
        self.prev = 0
        self.trigger = False # set the trigger off at the beginning

    def nxt(self):
        if self.trigger == False:
            # reset the values if the trigger is off
            self.val = 0
            self.prev = 0
            self.trigger = True
        if self.val == 0:
            self.val = 1
        elif self.val == 1 and self.prev == 0:
            self.val = 1
            self.prev = 1
        else:
            # fibonacci
            temp = self.val
            self.val = self.val + self.prev
            self.prev = temp
        return self
    def __repr__(self):
        self.trigger = False
        # set the trigger off again for the next execution
        return str(self.val)

a = Fibonacci()
print(a)
print(a.nxt())
print(a.nxt().nxt())
print(a.nxt().nxt().nxt())
print(a.nxt().nxt().nxt().nxt())
print(a.nxt().nxt().nxt().nxt().nxt())
print(a.nxt().nxt().nxt().nxt().nxt().nxt())