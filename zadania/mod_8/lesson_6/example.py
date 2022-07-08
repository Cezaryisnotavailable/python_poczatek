def check_is_number_in_list(number_to_check, all_numbers):
    for number in all_numbers:
        if number_to_check == number:
            print(f"{number_to_check} znaleziony!")
            break
    else:
        print(f"Nie znaleziono {number_to_check}")


# def check_is_number_in_list(number_to_check, all_numbers):
#     for number in all_numbers:
#         if number_to_check == number:
#             print(f"{number_to_check} znaleziony!")
#             return # przerywamy działanie całej funkcji, nie tylko for-a
#         else:
#             print(f"Nie znaleziono {number_to_check}")


def ask_for_even_nuber():
    number = 1
    while number % 2 != 0:
        number = int(input("wproawdz liczbe parzysta albo 1, zeby zakonczyc"))
        if number == 1:
            print("ok, konczymy")
            break
    else:
        print(f"twoja liczba to: {number}")


def run_example():
    check_is_number_in_list(7, [1, 5, 6, 7, 8, 9])
    check_is_number_in_list(115, [1, 5, 6, 7, 8, 9])
    ask_for_even_nuber()

if __name__ == "__main__":
    run_example()
