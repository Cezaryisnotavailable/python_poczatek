
sports_list = ["siatkówka", "piwo", "siłownia", "dziwki", "koks", "tajski boks"]

print(sports_list[1::2])


# drugie rozwiązanie
print("jakie są twoje ulubione sporty?")

favourite_sports = []

while True:
    sports = input("Podaj sport lub zakończ wpisując 'X': ")
    if sports == 'X':
        break
    else:
        favourite_sports.append(sports)

print(favourite_sports[1::2])