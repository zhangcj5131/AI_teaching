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
        print(self.martial_art)


if __name__ == '__main__':
    s = Student()
    s.show()
    print(Student.mro())