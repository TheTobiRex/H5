class Buttons_class:
    def Plus():
        Værdi1 = int(input("Vælg det første tal: "))
        Værdi2 = int(input("Vælg det andet tal: "))
        sum = Værdi1 + Værdi2
        print("Summen af de to tal er: " + str(sum))

    def Minus():
        Værdi1 = int(input("Vælg det første tal: "))
        Værdi2 = int(input("Vælg det andet tal: "))
        sum = Værdi1 - Værdi2
        print("Resultatet er: " + str(sum))

    def Gange():
        Værdi1 = int(input("Vælg det første tal: "))
        Værdi2 = int(input("Vælg det andet tal: "))
        sum = Værdi1 * Værdi2
        print("Resultatet er: " + str(sum))

    def Divider():
        Værdi1 = int(input("Vælg det første tal: "))
        Værdi2 = int(input("Vælg det andet tal: "))
        sum = Værdi1 / Værdi2
        print("Resultatet er: " + str(sum))

'''
class Meny_Class:
    def week(i):
        print("Vælg en regneart:")
        switcher = {
            "plus": Buttons_class.Plus(),
            "minus": 'Monday',
            "gange": 'Tuesday',
            "divider": 'Wednesday'
        }
        return switcher.get(i, "Invalid day of week")
'''