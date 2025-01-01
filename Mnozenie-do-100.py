from time import sleep

# Program that asks for a name and greets the user

number = int(input("Podaj Liczbę: "))
print("Teraz pomnożę tą liczbę od 1 do 30")
sleep(2)
for i in range(1, 31):
    print(f"{number} * {i} = {number * i}")
    sleep(0.5)
    print("kupsko")