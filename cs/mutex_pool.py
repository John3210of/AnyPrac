import threading
import time

class MutexPool:
    def __init__(self, size):
        self.mutexes = [threading.Lock() for _ in range(size)]

    def acquire_mutex(self):
        for mutex in self.mutexes:
            if mutex.acquire(blocking=False):
                return mutex
        return None

    def release_mutex(self, mutex):
        mutex.release()

def access_shared_resource(mutex, thread_name):
    print('im in mutex')
    with mutex:
        # 공유 자원에 대한 작업 수행
        print(f"공유 자원에 접근 중... Thread Name: {thread_name}")
        # 이 부분에 공유 자원에 대한 작업을 수행합니다.
        time.sleep(1)

# 여러 스레드에서 공유 자원에 접근
def thread_worker(mutex_pool, thread_name):
    mutex = mutex_pool.acquire_mutex()  # 뮤텍스 풀에서 뮤텍스를 얻습니다.
    if mutex:
        access_shared_resource(mutex, thread_name)  # 공유 자원에 접근하는 함수 호출
        mutex_pool.release_mutex(mutex)  # 뮤텍스 풀에 뮤텍스를 반환합니다.

mutex_pool = MutexPool(2)
threads = []
for i in range(5):
    thread_name = f"Thread-{i+1}"
    thread = threading.Thread(target=thread_worker, args=(mutex_pool, thread_name))
    threads.append(thread)
    thread.start()

# # 모든 스레드 종료 대기
# for thread in threads:
#     thread.join()
