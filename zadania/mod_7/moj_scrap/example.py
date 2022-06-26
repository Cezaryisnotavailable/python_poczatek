import requests


# def run_example():
#     response = requests.get("https://www.biznesradar.pl/akcjonariat/4MS")
#     print(response.status_code)
#     print(response.ok)
#
#     response.raise_for_status()
#     print(response.text)

def run_example():
    LICZBA_SPACJI = 18
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

    # print(response.text)
    # print(response.text.find("razem"))
    text = response.text
    razem_index = text.find("razem")
    start_from = text[razem_index:(razem_index + LICZBA_SPACJI)]
    index_start_from = razem_index + LICZBA_SPACJI
    index_stop = index_start_from + 5
    wanted_text = text[index_start_from:index_stop]
    print(wanted_text)





if __name__ == "__main__":
    run_example()