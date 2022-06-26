
def run_example():

    try:
        print("Przed rzuceniem wyjątku")
        raise TypeError("Cos poszlo nie tak")
        print("To sie nie wydarzy")
    except Exception as error:
        print(f"Jezeli wyjatek jest klasa potomna to tez zlapie: {error}")

    print("I program bedzie przetwarzany dalej")

if __name__ == '__main__':
    run_example()