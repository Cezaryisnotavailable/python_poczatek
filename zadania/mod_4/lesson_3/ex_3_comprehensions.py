
def run_example():
    numbers = [number for number in range(15)]
    print(numbers)
    print(len(numbers))

    # list comprehension z if-em
    numbers = [number for number in range(15) if number % 2 == 0]
    print(numbers)
    print(len(numbers))

    # w analogiczny sposób można wybrać co drugi smak
    favourite_flavours = [
        "malinowy",
        "truskawkowy",
        "czekoladowy",
        "pistacjowy",
        "kokosowy",
    ]
    flavours = [flavour for index, flavour in enumerate(favourite_flavours) if index % 2 == 0]
    print(flavours)

    # użycie pełnego wyrażenia if - else
    flavours = [flavour if index % 2 == 0 else "---" for index, flavour in enumerate(favourite_flavours)]
    print(flavours)


    #zagnieżdzanie comprehension
    rows_and_cols = [[row for row in range(5)]for column in range(4)]
    print(rows_and_cols)

    
    rows_and_cols = []
    for column in range(4):
        rows_and_cols.append([])
        for row in range(5):
            rows_and_cols[column].append(row)
    print(rows_and_cols)


if __name__ == '__main__':
    run_example()
