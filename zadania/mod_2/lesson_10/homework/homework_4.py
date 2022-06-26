from homework_2 import any_length_kwargs

dict_1 = {
    "hiszpański": 4,
    "niemiecki": 1
}

dict_2 = {
    "marokański": 4,
    "ukrapoliński": 1
}

dudu = {**dict_1, **dict_2}
print(dudu)
any_length_kwargs(**dudu)
