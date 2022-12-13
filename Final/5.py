class Student():
    def __init__(self, name = '', number = 0):
        self.name = name
        self.course = number
    def __add__(self, other):
        res = Student()
        res.course = self.course + other.course
        return res
    def __repr__(self):
        return str(self.course)
    def __lt__(self, other):
        return self.course < other.course
    def __gt__(self, other):
        return self.course > other.course
    def __eq__(self, other):
        return self.course == other.course
    def __ne__(self, other):
        return self.course != other.course



a = Student('Peter', 3)
b = Student('Mike', 4)
c = Student('John', 5)
d = Student('Kelvin', 3)
print(a+b+d) # 10
print(a+b+c+d) # 15
print(a!=d) # False
print(b<c) # True