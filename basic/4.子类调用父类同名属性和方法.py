class Master:
    def __init__(self):
        self.martial_art = 'kongfu'

    def show(self):
        print(self.martial_art)


class School:
    def __init__(self):
        self.martial_art = 'boxing'

    def show(self):
        print(self.martial_art)

class Student(School, Master):
    def __init__(self):
        self.martial_art = 'free combat'

    def show(self):
        self.__init__()
        print(self.martial_art)

    def show_boxing(self):
        School.__init__(self)
        School.show(self)

    def show_kongfu(self):
        Master.__init__(self)
        Master.show(self)


if __name__ == '__main__':
    s = Student()
    s.show_boxing()
    s.show()
    s.show_kongfu()
    # print(Student.mro())