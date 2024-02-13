from abc import ABC, abstractmethod

class Vtak(ABC):
    @abstractmethod
    def lietaj(self):
        pass

    @abstractmethod
    def chod(self):
        pass

class Pstros(Vtak):
    def fly(self):
        raise Exception("Pstros is not flying")

    def walk(self):
        print("Pstros is walking")

class Orol(Vtak):
    def fly(self):
        print("Orol is flying")

    def walk(self):
        print("Orol is walking")

try:
    obj = Orol()
    obj.fly()
    obj.walk()
    obj2 = Pstros()
    obj2.walk()
    obj2.fly()
except Exception as e:
    print(e)