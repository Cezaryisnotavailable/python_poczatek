import random

def random_list():
    list = []
    for _ in range(random.randint(1, 10)):
        list.append(random.randint(1, 1000))
    return list

def run_homework():


    list_1 = random_list()
    list_2 = random_list()
    print(list_1, list_2)

    all_list = [*list_1, *list_2]
    print(all_list)


if __name__ == "__main__":
    run_homework()



