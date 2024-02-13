from abc import ABC, abstractmethod

class Zviera(ABC):
    @abstractmethod
    def zvuk(self):
        pass

class Pes(Zviera):
    def zvuk(self):
        return "Haf"

moje_zviera = Zviera()

moj_pes = Pes()
print(moj_pes.zvuk())