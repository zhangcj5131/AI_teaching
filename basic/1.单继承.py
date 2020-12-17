class Master(object):
    def __init__(self):
        self.martial_art = "Kongfu"

    def show(self):
        print('my genre is %s' % self.martial_art)


class Student(Master):
    pass
if __name__ == '__main__':
    s = Student()
    s.show()
