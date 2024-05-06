class Human():
    def __init__(self,age) -> None:
        self.age = age
    def get_next_age(self):
        print('next age = ',self.age+1)
    def start(self):
        print('human definition')
        self.get_next_age()
    
class HuHuman(Human):
    def get_next_age(self):
        super().get_next_age()
        print('im huhuman get next age ')


hu=Human(age=10)
hu.start()

huhu=HuHuman(age=20)
huhu.start()