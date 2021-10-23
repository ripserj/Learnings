class Tanks():
    def view(self):
        print("Its, Tanks!")

class HeavyTanks(Tanks):

    def view(self):
        super().view()
        print("Its, Heavy Tanks!")

class LightTanks(Tanks):

    def view(self):
        super().view()
        print("Its, Light Tanks!")

class GeneralTanks(LightTanks, HeavyTanks):

    def view(self):
        super().view()
        print("Its, General Tanks!")

unit_1 = GeneralTanks()
unit_1.view()
print(unit_1.__class__.__mro__)
