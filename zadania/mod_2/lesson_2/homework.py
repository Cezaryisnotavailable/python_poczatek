
class Produkt:
    pass


class Zamówienia:
    pass


class Jabłko:
    pass


class Ziemniak:
    pass


jablko_1 = Jabłko()
jablko_2 = Jabłko()

ziemniak_1 = Ziemniak()
ziemniak_2 = Ziemniak()

print(type(jablko_1))
print(type(ziemniak_1))


lista_zamowien = [Zamówienia(), Zamówienia(), Zamówienia(), Zamówienia(), Zamówienia()]
print(lista_zamowien)

slownik_produktow = {
    "kubek": Produkt(),
    "telefon": Produkt(),
    "okulary": Produkt()
}
print(slownik_produktow)
