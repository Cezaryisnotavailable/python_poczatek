
def any_length_args(*args):
    napis = ""
    for arg in args:
        napis += f"{arg}-"
    return napis[:-1]

def run_homework():

    napis = any_length_args(1, 2, 3, 4, 5, 6, "hello")
    print(napis)
    print(type(napis))


if __name__ == "__main__":
    run_homework()