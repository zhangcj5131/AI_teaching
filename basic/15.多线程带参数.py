'''
进程
1.进程是系统分配资源的最小单位,一个进程一旦创立就会需要分配资源.比较耗资源.
2.各个进程之间无法通信,也无法共享任何资源,哪怕是全局变量的数据,进程间也无法共享

线程
1.线程是程序执行的最小单位,进程负责分配资源,线程负责执行程序
2.可以认为,进程是线程的容器,一个进程里至少需要有一个线程
3.线程本身不拥有系统资源,
4.属于同一个进程的多个线程之间可以共享资源.
'''


import threading
import time

# 唱歌任务
def sing(num):
    # 扩展： 获取当前线程
    # print("sing当前执行的线程为：", threading.current_thread())
    for i in range(num):
        print("sing %d" % i)
        time.sleep(1)

# 跳舞任务
def dance(count):
    # 扩展： 获取当前线程
    # print("dance当前执行的线程为：", threading.current_thread())
    for i in range(count):
        print("dangcing %d" % i)
        time.sleep(1)


if __name__ == '__main__':
    # 扩展： 获取当前线程
    # print("当前执行的线程为：", threading.current_thread())
    # 创建唱歌的线程
    # target： 线程执行的函数名
    sing_thread = threading.Thread(target=sing, args = (5,))

    # 创建跳舞的线程
    dance_thread = threading.Thread(target=dance, kwargs={'count':4})

    # 开启线程
    sing_thread.start()
    dance_thread.start()