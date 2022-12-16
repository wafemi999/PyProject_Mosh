class Person:
    def __init__(self,name):
        self.name = name


    def talk(self):
        print(f'i am {self.name}')



person1 = Person('manuel')


person1.talk()
