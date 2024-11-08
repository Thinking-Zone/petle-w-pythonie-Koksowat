import random
pogoda = random.choice([True, False])
while True:
    odpowiedz = input("Czy pada deszcz? (tak/nie): ").strip().lower()
    if odpowiedz == "tak" and pogoda:
        print("Brawo! Zgadłeś, pada deszcz!")
        break
    elif odpowiedz == "nie" and not pogoda:
        print("Brawo! Zgadłeś, nie pada deszcz!")
        break
    else:
        print("Niestety, spróbuj ponownie.")
