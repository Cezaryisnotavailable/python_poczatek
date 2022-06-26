
def run_example():
    # W przykładzie wykorzystamy listę ulubionych smaków ;)
    favourite_flavours = [
        "malinowy",
        "truskawkowy",
        "czekoladowy",
        "pistacjowy",
        "kokosowy",
    ]

    print(favourite_flavours)

    favourite_flavours.reverse()
    print(favourite_flavours)

    print(favourite_flavours.count("malinowy"))

    copy_of_flavours = favourite_flavours.copy()

    new_flavours = ["orzechowy", "jagodowy"]
    copy_of_flavours.extend(new_flavours)


if __name__ == '__main__':
    run_example()
