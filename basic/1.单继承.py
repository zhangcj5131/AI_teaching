class Master:
    def __init__(self):
        self.martial_art = 'kongfu'

    def show(self):
        print(self.martial_art)


class Student(Master):
    pass


if __name__ == '__main__':
    s = Student()
    s.show()