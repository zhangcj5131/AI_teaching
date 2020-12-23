import multiprocessing
import time


# 跳舞任务,这个方法有参数
def dance(num, name):
    print(name)
    for i in range(num):
        print("跳舞中...")
        time.sleep(0.2)


# 唱歌任务,这个方法有参数
def sing(count):
    for i in range(count):
        print("唱歌中...")
        time.sleep(0.2)

if __name__ == '__main__':
    # 创建跳舞的子进程
    # group: 表示进程组，目前只能使用None
    # target: 表示执行的目标任务名(函数名、方法名)
    # name: 进程名称, 默认是Process-1, .....
    #如果需要传参,用kwargs参数传递参数
    dance_process = multiprocessing.Process(target=dance, name="myprocess1", args=(3,'zhangsan'))
    sing_process = multiprocessing.Process(target=sing, kwargs={'count':9})

    # 启动子进程执行对应的任务
    dance_process.start()
    sing_process.start()