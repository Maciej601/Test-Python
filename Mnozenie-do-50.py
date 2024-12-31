from time import sleep

# Program that asks for a name and greets the user

number = int(input("Podaj Liczbę: "))
for i in range(1, 101):
    print(f"{number} * {i} = {number * i}")
    sleep(0.5)
