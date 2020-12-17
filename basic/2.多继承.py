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
    pass


if __name__ == '__main__':
    s = Student()
    s.show()
    print(Student.mro())