class Student:
    def __init__(self):
        self.math = 95
        self.english = 90

    def set_chinese(self, score):
        self.chinese = score


student = Student()
student.set_chinese(70)
chinese = student.chinese
print(chinese)

