
def run_example():
    with open("plain_text.txt", mode="r") as plain_text_file:
        print(plain_text_file.read(25)) # 25 to liczba bajtów
        print(plain_text_file.read(25))


if __name__ == "__main__":
    run_example()
