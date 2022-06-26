
from collections import namedtuple

Location = namedtuple("Location", ["latitude", "longitude"])

def run_example():
    location = Location(10.01, 30.65)
    print(location.latitude)
    print(location.longitude)
    print(type(location))

    print(location[0])
    for coordinate in location:
        print(coordinate)

if __name__ == '__main__':
    run_example()