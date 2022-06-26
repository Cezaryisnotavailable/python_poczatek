
class LettersParsingError(Exception):
    pass


def first_three_letters(letters_str):
    try:
        check = letters_str.isalpha()
        if check is not True:
            raise ValueError
    except ValueError:
        raise LettersParsingError("Przekazany argument nie jest literą")

    if len(letters_str) != 3:
        raise LettersParsingError("Przekazany argument nie ma dokłądnie 3 znaków")

    print("Dziekuje, zaraz poznasz magiczny wynik")


def run_homework():
    letters_str = input("pierwsze trzy litery imienia")

    try:
        first_three_letters(letters_str)
    except LettersParsingError as error:
        print(error)
    else:
        result = 3 * letters_str
        print(f"Wynik magicznego dzialania to {result[::-1]}")
    finally:
        print("Konczy program...")




if __name__ == "__main__":
    run_homework()