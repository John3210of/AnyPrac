import threading
import time

def access_shared_resource(mutex,name='default'):
    # 뮤텍스 획득
    mutex.acquire()
    try:
        # 공유 자원에 대한 작업 수행
        print(f"공유 자원에 접근 중...{name}")
        # 이 부분에 공유 자원에 대한 작업을 수행합니다.
        time.sleep(3)
    finally:
        # 뮤텍스 해제
        mutex.release()

# 뮤텍스 생성
mutex = threading.Lock()
# 여러 스레드에서 공유 자원에 접근
thread1 = threading.Thread(target=access_shared_resource,args=(mutex,'Thread1'))
thread2 = threading.Thread(target=access_shared_resource,args=(mutex,'Thread2'))
thread1.start()
thread2.start()

thread1.join()
thread2.join()