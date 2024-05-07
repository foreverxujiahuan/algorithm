

# 定一个student类，包含学生的姓名，年龄、身高、体重、语文成绩、数学成绩、学生的平均成绩

class People:
    def __init__(self,
                 sex):
        self.sex = sex


class Student(People):

    def __init__(self, sex, name, age, height, weight, chinese, math):
        super().__init__(sex)
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.chinese = chinese
        self.math = math

    def say_hello(self):
        print(f"hello, My name is {self.name}")

    def get_ave_score(self):
        return (self.chinese + self.math) / 2

    def __len__(self):
        return len(self.name)

    def __getitem__(self, k):
        if k == "语文":
            return self.chinese
        elif k == "数学":
            return self.math
        else:
            return "成绩不存在"


if __name__ == '__main__':
    xiao_ming = Student(name="小明",
                        sex="male",
                        age=12,
                        height=155,
                        weight=100,
                        chinese=96,
                        math=80)
    # print(xiao_ming.__len__())
    # print(len(xiao_ming))
    # print(xiao_ming['数学'])
    # print(xiao_ming.__getitem__("数学"))
    # print(getitem(xiao_ming))
    # a = [1,2,3]
    # l = len(a)

    # xiao_hong = Student(name="小红",
    #                     sex="female",
    #                     age=12,
    #                     height=148,
    #                     weight=85,
    #                     chinese=98,
    #                     math=85)
    # # print(xiao_ming.get_ave_score())
    # # print(xiao_hong.get_ave_score())
    # # xiao_ming.say_hello()
    # print(xiao_ming.say_hello())
    # print(xiao_ming.name)
    # print(xiao_ming.sex)
