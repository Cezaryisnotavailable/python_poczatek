import random


def random_id():
    id_number = random.randint(1,999)
    whole_od_number = str(id_number).zfill(5)
    print(whole_od_number)


def run_homework():
    random_id()

if __name__ == "__main__":
    run_homework()
