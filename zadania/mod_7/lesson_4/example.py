import requests


# def run_example():
#     response = requests.get("https://www.biznesradar.pl/akcjonariat/4MS")
#     print(response.status_code)
#     print(response.ok)
#
#     response.raise_for_status()
#     print(response.text)

def run_example():
    try:
        response = requests.get("https://www.biznesradar.pl/akcjonariat/4MS")
    except requests.RequestException as error:
        print(f"Błąd przy połączeniu: {error}")
        return

    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        print(f"Żądanie zakończone niepowodzeniem {error}")
        return

    print(response.text)






if __name__ == "__main__":
    run_example()