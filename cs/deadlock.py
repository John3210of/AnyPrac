# 식사하는 철학자 구현
import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.running = True
    def run(self):
        while self.running:
            time.sleep(random.uniform(1, 3)) # 랜덤하게 식사를 시작
            print(f'{self.name} is hungry.')
            self.dine()
    def dine(self):
        fork1, fork2 = self.left_fork, self.right_fork
        while self.running:
            # 철학자는 왼쪽 포크와 오른쪽 포크를 동시에 집지 않고
            # 한 번에 하나씩 집어야 교착상태(deadlock)가 발생하지 않습니다.
            # 1개를 잡고, 2개째를 잡을수 있는지에대해 기다리지않고 바로 판단.
            # 점유와 대기를 부정하는 방식으로 구현
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: # >> 오른쪽 포크가 True일때,
                # 식사 시작
                self.dining()
                fork2.release()  # 식사가 끝나면 포크를 모두 놓음
                fork1.release()
                self.running = False
                break
            fork1.release()  # 오른쪽 포크를 획득하지 못한 경우 왼쪽 포크를 다시 놓음
        
    def dining(self):
        #식사시간은 랜덤
        print(f'{self.name} starts eating')
        time.sleep(random.uniform(1, 3))
        print(f'{self.name} finishes eating and leaves to think.')

    def is_finished(self) -> bool:
        return not self.running

def main():
    forks = [threading.Lock() for _ in range(5)]  # 포크는 5개, 공유자원으로 선언
    philosophers = []
    for i in range(5):
        philosopher = Philosopher(f'Philosopher {i}', forks[i % 5], forks[(i + 1) % 5])
        philosophers.append(philosopher)
        philosopher.start() # start는 thread를 할당하기 위해서 무조건 실행해야하고, 내부적으로 run()을 실행한다.
        '''
        def start(self):
            ...
            try:
                 _start_new_thread(self._bootstrap, ())
                 >>  def _bootstrap(self):
                        try:
                            self._bootstrap_inner()
                        >>  try:
                                self.run()
        '''

if __name__ == "__main__":
    main()
# 스레드를 여러개 부여한다.
# 공유자원에 대해 각쓰레드에서 접근한다.
# 왼쪽에 대해서는 기다리고, 오른쪽에 대해서는 즉시 사용할수 없다면 더 기다리지 않음