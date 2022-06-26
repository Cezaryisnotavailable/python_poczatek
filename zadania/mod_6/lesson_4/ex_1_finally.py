
class NumberParsingError(Exception):
    pass


def handle_even_number(number_str):
    try:
        number = int(number_str)
    except ValueError:
        raise NumberParsingError("Przekazany argument nie jest liczba")

    if number % 2 != 0:
        raise NumberParsingError("Podana liczba nie jest parzysta")

    print(f"Dzieki. Podana liczba podzielona przez 2 to: {number/2}")


def run_example():
    number_str = input("podaj liczbe parzysta")

    # try:
    #     handle_even_number(number_str)
    # finally:
    #     print("Bledu nie zlapiemy, ale to wypisze sie zawsze")

    try:
        handle_even_number(number_str)
    except NumberParsingError as error:
        print(error)
        raise error
    finally:
        print("Bledu nie zlapiemy, ale to wypisze sie zawsze")



if __name__ == "__main__":
    run_example()