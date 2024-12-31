from time import sleep

# Program that asks for a name and greets the user

number = int(input("Enter a number: "))
for i in range(1, 51):
    print(f"{number} * {i} = {number * i}")
    sleep(0.5)