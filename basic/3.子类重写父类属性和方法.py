class Master(object):
    def __init__(self):
        self.martial_art = "Kongfu"

    def show(self):
        print('my genre is %s' % self.martial_art)

class School(object):
    def __init__(self):
        self.martial_art = "boxing"

    def show(self):
        print('my genre is %s' % self.martial_art)


class Student(School, Master):
    def __init__(self):
        self.martial_art = "free combat"

    def show(self):
        print('my genre is %s' % self.martial_art)

if __name__ == '__main__':
    s = Student()
    s.show()