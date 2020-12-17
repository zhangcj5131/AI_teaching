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

    def show_all(self):
        self.__init__()
        self.show()

        Master.__init__(self)
        Master.show(self)

        School.__init__(self)
        School.show(self)

class Tusun(Student):
    pass

if __name__ == '__main__':
    s = Tusun()
    s.show_all()
    # s.show()
    # s.show_kongfu()
    # s.show_boing()
    # print(Student.mro())