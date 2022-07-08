# Zaimplementuj program, który wczyta od użytkownika liczbę w systemie dziesiętnym i wypisze ją w notacji z
# podkreśleniami notacji ósemkowej oraz szesnastkowej.

def run_homework():

    def convert(number_in_string):
        number_str = ""
        start_index = 0
        next_index = 1
        for _ in range(len(number_in_string)):
            if start_index % 3 == 0 and start_index != 0:
                number_str += "_"
            number_str += number_in_string[start_index:next_index]
            start_index += 1
            next_index += 1
        print(number_str)

    given_number = int(666666)
    number_oct = oct(given_number)
    number_hex = hex(given_number)
    convert(number_oct)
    convert(number_hex)








if __name__ == '__main__':
    run_homework()
