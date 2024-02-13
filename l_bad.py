class Vtak:
    def lietat(self):
        pass

class Vrabec(Vtak):
    def lietat(self):
        return "Vrabec lieta"

class Kura(Vtak):
    def lietat(self):
        return "Kura nemôže lietať"

def spustit_lietanie(vtak):
    print(vtak.lietat())

vrabec = Vrabec()
kura = Kura()

spustit_lietanie(vrabec)
spustit_lietanie(kura)