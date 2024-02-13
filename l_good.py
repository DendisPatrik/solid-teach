class Vtak:
    pass

class LietajuciVtak(Vtak):
    def lietat(self):
        pass

class Vrabec(LietajuciVtak):
    def lietat(self):
        return "Vrabec lieta"

class Kura(Vtak):
    pass

def spustit_lietanie(lietajuci_vtak):
    print(lietajuci_vtak.lietat())

vrabec = Vrabec()
spustit_lietanie(vrabec)