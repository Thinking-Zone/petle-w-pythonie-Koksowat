liczba_nie = 0

while True:
    odpowiedz = input("Czy pada? (tak/nie/nie wiem): ").strip().lower()

    if odpowiedz == "tak":
        print(f"Zakończono! Udzieliłeś {liczba_nie} odpowiedzi 'nie'.")
        break
    elif odpowiedz == "nie":
        liczba_nie += 1
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")
