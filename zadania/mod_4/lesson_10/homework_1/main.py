from collections import namedtuple

CounterApple = namedtuple("CounterApple", ["species_name", "size", "price"])

def run_homework():
    counter_apple = CounterApple("jabłko", "S", 5)
    print(counter_apple.species_name, counter_apple.size, counter_apple.price)
    print(counter_apple[1])
    print(counter_apple[2])

    for param in counter_apple:
        print(param)








if __name__ == '__main__':
    run_homework()
