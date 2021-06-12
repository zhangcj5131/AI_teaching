

# def is_target(n: int):
#     if n % 7 == 0 and n % 5 != 0:
#         return True
#     return False
#
#
# def get_num(a = 2000, b = 3001):
#     mylist = []
#     for i in range(a, b):
#         if is_target(i):
#             mylist.append(str(i))
#     return mylist
#
# mylist = get_num(2,89)
# print(','.join(mylist))
# for c in mylist:
#     print(c, end=',')


# def myfact(n:int):
#     if n == 0 or n == 1:
#         return 1
#     return n*myfact(n-1)
# print(myfact(3))


# def my_dict(n: int):
#     mydict = {}
#     for i in range(1, n+1):
#         mydict[i] =  i**2
#     return mydict
#
# mydict = my_dict(8)
# print(mydict)

class StringOperation:
    def __init__(self):
        self.s = None

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


mystr = StringOperation()
mystr.getString()
mystr.printString()
