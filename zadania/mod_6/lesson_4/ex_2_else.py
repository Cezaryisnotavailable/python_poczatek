
class NumberParsingError(Exception):
    pass


def handle_even_number(number_str):
    try:
        number = int(number_str)
    except ValueError:
        raise NumberParsingError("Przekazany argument nie jest liczba")

    if number % 2 != 0:
        raise NumberParsingError("Podana liczba nie jest parzysta")

    return number/2


def run_example():
    number_str = input("podaj liczbe parzysta")

    try:
        parsed_number = handle_even_number(number_str)
    except NumberParsingError as error:
        print(error)
    else:
        result = 100 / parsed_number
        print(f"Wynik magicznego dzialania to {result}")
    finally:
        print("Konczy program...")




if __name__ == "__main__":
    run_example()