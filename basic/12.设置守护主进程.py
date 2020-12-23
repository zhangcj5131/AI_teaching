import multiprocessing
import time
'''
主进程会等待所有子进程都结束以后再结束
'''
def work():
    for i in range(10):
        print('working')
        time.sleep(0.2)

if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    #当子进程发现主进程已经结束了,就自动终止自己.
    work_process.daemon = True
    work_process.start()

    time.sleep(1)
    print('mian process is over')
