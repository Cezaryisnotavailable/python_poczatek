
def run_example():

    try:
        print("Przed rzuceniem wyjątku")
        raise TypeError("Cos poszlo nie tak")
        print("To sie nie wydarzy")
    except ValueError as error:
        print(f"Wyjatek nie zostanie wypisany, bo nie pasuje jego typ")

    print("I program bedzie przetwarzany dalej")

if __name__ == '__main__':
    run_example()