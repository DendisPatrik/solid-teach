from abc import ABC, abstractmethod

class Walkable(ABC):
    @abstractmethod
    def chod(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def lietaj(self):
        pass

class Pstros(Walkable):
    def chod(self):
        print("Pstros is walking")

class Orol(Walkable, Flyable):
    def lietaj(self):
        print("Orol is flying")
    def chod(self):
        print("Orol is walking")

try:
    obj = Orol()
    obj.lietaj()
    obj.chod()

    obj2 = Pstros()
    obj2.chod()

except Exception as e:
    print(e)