
def clean_print(name, surname):
    name = str(name).strip()
    surname = str(surname).strip()
    print(f"Nazywasz się {name} {surname} - jak miło Cię poznać :)")


def run_homework():
    clean_print("Jan  ", "    Masłowski")


if __name__ == "__main__":
    run_homework()
