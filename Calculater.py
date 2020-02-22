import Calculater


Regneart = input("Vælg en regneart: ")

if Regneart == "plus":
    Calculater.Buttons_class.Plus()
elif Regneart == "minus":
    Calculater.Buttons_class.Minus()
elif Regneart == "gange":
    Calculater.Buttons_class.Gange()
elif Regneart == "divider":
    Calculater.Buttons_class.Divider()