import threading
import time
lock = threading.Lock()
def run(number):
    lock.acquire()
    print('%s…… starting '%number)
    time.sleep(2)
    print('____________')
    lock.release()
if __name__ == '__main__':
    print('___主线程开始___',threading.current_thread().name)
    thread_list=[]
    for i in range(1,5):
        t = threading.Thread(target= run,args=(i,))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    print('___主线程结束___',threading.current_thread().name)
