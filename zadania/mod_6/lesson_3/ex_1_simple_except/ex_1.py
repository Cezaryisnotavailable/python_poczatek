
def run_example():

    try:
        print("Przed rzuceniem wyjątku")
        raise TypeError("Cos poszlo nie tak")
        print("To sie nie wydarzy")
    except TypeError:
        print("Ale złapaliśmy wyjątek")

    print("I program bedzie przetwarzany dalej")

if __name__ == '__main__':
    run_example()