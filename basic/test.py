class Master(object):
    def __init__(self):
        self.martial_art = 'Master'

    def show(self):
        print(self.martial_art)

class School(object):
    def __init__(self):
        super().__init__()
        self.martial_art = 'School'

    def show(self):
        print(self.martial_art)
        super().__init__()
        super().show()


class Student(School, Master):
    def __init__(self):
        self.martial_art = 'student'

    def show(self):
        self.__init__()
        print(self.martial_art)


    def show_all(self):
        print(self.martial_art)
        super().__init__()
        super().show()



if __name__ == '__main__':
    s = Student()
    s.show_all()

