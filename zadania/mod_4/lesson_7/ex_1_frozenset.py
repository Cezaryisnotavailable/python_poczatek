
def run_example():
    flavours = ["Malinowy", "Truskawkowy", "Jagodowy"]
    bob_favourite_flavours = frozenset(flavours)
    print(type(bob_favourite_flavours))

    alice_favourite_flavours = frozenset({"Pistacjowy", "Truskawkowy", "Orzechowy"})
    print(alice_favourite_flavours)

    #duplikaty
    alice_favourite_flavours = frozenset(["Pistacjowy", "Truskawkowy", "Orzechowy", "Orzechowy", "Orzechowy"])
    print(alice_favourite_flavours)

    #chyba wspólne smaki
    common_flavours = bob_favourite_flavours.intersection(alice_favourite_flavours)
    print(common_flavours)
    all_flavours = bob_favourite_flavours.union(alice_favourite_flavours)
    print(all_flavours)

    # robienie zbioru zbiorów
    set_of_sets = {frozenset({"Słony karmel", "Mango"}), frozenset({"Truskawkowy", "Śmietankowy"})}
    print(type(set_of_sets))
    print(set_of_sets)

if __name__ == '__main__':
    run_example()