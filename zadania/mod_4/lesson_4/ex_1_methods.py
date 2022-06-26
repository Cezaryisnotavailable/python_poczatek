
def run_example():
    expenditures = {
        "prąd": [250],
        "woda": [30.45],
        "zakupy": [
            120.15,
            170.53,
            20.15
        ]
    }
    print(expenditures)

    expenditures_copy = expenditures.copy()

    cookies_expenditures = expenditures.get("ciasteczka")
    #pojawi się None, nie wyskoczy błąd tak jak gdyby było expeditures["ciasteczka"]
    print(cookies_expenditures)

    cookies_expenditures = expenditures.get("ciasteczka", "nie ma ciasteczek")
    print(cookies_expenditures)

    expenditures.update(jedzenie=[120], rozrywka=[120])
    print(expenditures)


if __name__ == "__main__":
    run_example()