
# f = open('//Users/cjz/class/aa.txt')
# # s = f.readline()
# # print(s)

# coding=utf-8
globalInt = 9
#定义一个函数
def myAdd():
       #在函数中定义一个局部变量
	localInt = 3
	global gi
	gi =7
	return globalInt + localInt
#测试变量的局部性和全局性
print(myAdd())
print (globalInt)
# print( gi )
# print(localInt )