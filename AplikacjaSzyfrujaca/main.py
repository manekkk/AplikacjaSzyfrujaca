import random
import string

znaki = string.ascii_letters + string.digits + string.punctuation + string.whitespace
znaki = list(znaki)
cyk = znaki.copy()

random.shuffle(cyk)

print(f"znaki : {znaki}")
print(f"klucze : {cyk}")
#########szyfrowanie
tekst_zwykly =  input("Wpisz tekst do zaszyfrowania: ")
zaszyfrowanie = ""

for x in tekst_zwykly:
    indeks = znaki.index(x)
    zaszyfrowanie += cyk[indeks]

print(f"normalny tekst : {tekst_zwykly}")
print(f"zaszyfrowanie : {zaszyfrowanie}")
##########odszyfrowywanie
zaszyfrowanie =  input("Wpisz tekst do odszyfrowania: ")
tekst_zwykly = ""

for x in zaszyfrowanie:
    indeks = cyk.index(x)
    tekst_zwykly += znaki[indeks]

print(f"zaszyfrowanie : {zaszyfrowanie}")
print(f"normalny tekst : {tekst_zwykly}")
