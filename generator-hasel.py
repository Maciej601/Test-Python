import secrets
import string
import random

letters = string.ascii_letters # litery
digits = string.digits # cyfry
special_chars = string.punctuation # znaki specjalne
selection_list = letters + digits + special_chars # lista znaków do wyboru

password_len = 10 # długość hasła

password = '' # zmienna przechowująca hasło
for i in range(password_len): # pętla tworząca hasło
    password+= ''.join(secrets.choice(selection_list)) # dodanie losowego znaku do hasła
print("Oto twoje hasło: ") 
print(password) # wyświetlenie hasła