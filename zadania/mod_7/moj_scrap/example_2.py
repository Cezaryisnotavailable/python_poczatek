import requests
from bs4 import BeautifulSoup

def run_example():
    respose = requests.get("https://www.biznesradar.pl/akcjonariat/4MS")
    parsed_page = BeautifulSoup(respose.text, features="html.parser")


    tag_p = parsed_page.p
    print(tag_p)
    tag_td = parsed_page.td
    print(tag_td.string)
    proba = parsed_page.main.div.table
    print(proba.contents)
    print(proba.find_all("td"))




if __name__ == "__main__":
    run_example()