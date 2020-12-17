class Master(object):
    def __init__(self):
        self.martial_art = 'kongfu'

    def show(self):
        print('my gener is %s' % self.martial_art)

class School(object):
    def __init__(self):
        self.martial_art = 'boxing'

    def show(self):
        print('my gener is %s' % self.martial_art)


class Student(School, Master):
    def __init__(self):
        self.martial_art = 'free combat'

    def show(self):
        self.__init__()
        print('my gener is %s' % self.martial_art)

    def show_kongfu(self):
        Master.__init__(self)
        Master.show(self)

    def show_boing(self):
        School.__init__(self)
        School.show(self)


if __name__ == '__main__':
    s = Student()
    s.show()
    s.show_kongfu()
    s.show_boing()
    # print(Student.mro())