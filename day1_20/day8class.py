from time import sleep
class Student(object):
    # 构造函数和属性写一起了
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('bear is coming')
        else:
            print('av')

def main1():
    stu1 = Student('zf', 24)
    stu1.study('python')
    stu1.watch_movie()
    stu2 = Student('zht', 15)
    stu2.study('java')
    stu2.watch_movie()
class Clock(object):
    def __init__(self):
        self.id=id;


if __name__ == '__main__':
    main1()
