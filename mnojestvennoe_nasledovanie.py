class Tanks():
    def view_me(self):
        print("Its, Tanks!")

class HeavyTanks(Tanks):

    def view_me(self):
        super().view_me()
        print("Its, Heavy Tanks!")

class LightTanks(Tanks):

    def view_me(self):
        super().view_me()
        print("Its, Light Tanks!")

class GeneralTanks(LightTanks, HeavyTanks):

    def view_me(self):
        super().view_me()
        print("Its, General Tanks!")

class Aeroplanes():
    pass

unit_1 = GeneralTanks()
unit_1.view_me()
print(unit_1.__class__.__mro__)
unit_2 = LightTanks()
unit_2.veiw_me()
unit_3 = HeavyTanks()
unit_3.veiw_me()

unit_4 = GeneralTanks()
print(unit_4)
