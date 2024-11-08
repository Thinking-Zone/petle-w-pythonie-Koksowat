print("A pod spodem rozwiązanie tego zadanka, napisane w Pythonie :)")

suma = 0

for liczba in range(1, 201):
    if liczba % 2 == 0 and liczba % 5 == 0:
        suma += liczba

print("Suma liczb parzystych i podzielnych przez 5 w zakresie od 1 do 200 to:", suma)
