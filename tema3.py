# functii_studenti.py

def suma_cifrelor(n: int) -> str:

    if not isinstance(n, int):
        return "Eroare: Parametrul trebuie să fie un număr întreg."

    numar_pozitiv = abs(n)
    suma = 0

    if numar_pozitiv == 0:
        return f"Suma cifrelor numărului {n} este 0."

    temp_n = numar_pozitiv
    while temp_n > 0:
        cifra = temp_n % 10
        suma += cifra
        temp_n //= 10

    return f"Suma cifrelor numărului {n} este {suma}."

if __name__ == '__main__':
    print(suma_cifrelor(12345))
    print(suma_cifrelor(50005))
    print(suma_cifrelor(0))
    print(suma_cifrelor(-987))

    print(suma_cifrelor("text"))
    print(suma_cifrelor(12.5))

def cmmdc(a: int, b: int) -> str:

    if not isinstance(a, int) or not isinstance(b, int):
        return "Eroare: Ambii parametri trebuie să fie numere întregi."

    if a == 0 and b == 0:
        return "Eroare: CMMDC(0, 0) nu este definit. Vă rugăm să introduceți cel puțin un număr diferit de zero."

    numar_a = abs(a)
    numar_b = abs(b)

    x, y = numar_a, numar_b

    if x == 0:
        rezultat = y
    elif y == 0:
        rezultat = x
    else:
        while y:
            x, y = y, x % y
        rezultat = x

    return f"CMMDC({a}, {b}) = {rezultat}."


if __name__ == '__main__':
    print("--- Teste CMMDC ---")

    print(cmmdc(24, 36))  # Rezultat: 12

    print(cmmdc(12, 18))  # Rezultat: 6
    print(cmmdc(100, 30))  # Rezultat: 10
    print(cmmdc(7, 5))  # Rezultat: 1
    print(cmmdc(42, 0))  # Rezultat: 42
    print(cmmdc(0, 42))  # Rezultat: 42
    print(cmmdc(-12, 18))  # Rezultat: 6

    # Cazul special (0, 0)
    print(cmmdc(0, 0))  # Rezultat: Eroare

    print(cmmdc(12.5, 18))  # Rezultat: Eroare
    