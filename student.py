import random
class Student():
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.balance = 0
        self.cradit = 127
        self.id = random.randint(1,99)


stu1 = Student("Mr Sakib",22)
print(stu1.name)
print(stu1.age)
print(stu1.id)