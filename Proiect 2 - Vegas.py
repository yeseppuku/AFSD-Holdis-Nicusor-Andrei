import random
import matplotlib.pyplot as plt


# 1. Generarea datelor de intrare
def genereaza_date(n):
    vector = list(range(1, n + 1))
    random.shuffle(vector)  # Ordinea initiala nu conteaza oricum
    valoare_cautata = random.choice(vector)
    return vector, valoare_cautata


# 2. Implementarea căutării randomizate
def cautare_las_vegas(vector, valoare):
    n = len(vector)
    # Generam o permutare aleatoare a indicilor
    indici_aleatori = random.sample(range(n), n)

    pasi = 0
    for idx in indici_aleatori:
        pasi += 1
        if vector[idx] == valoare:
            return idx, pasi
    return -1, pasi  # Nu ar trebui sa se ajunga aici teoretic


# 3. Rulări multiple pentru același input
print("=== Rulari multiple pentru n = 1000 ===")
vector_test, valoare_test = genereaza_date(1000)
pasi_rulari = []

for _ in range(30):
    _, pasi = cautare_las_vegas(vector_test, valoare_test)
    pasi_rulari.append(pasi)

print(f"Numar minim de pasi: {min(pasi_rulari)}")
print(f"Numar maxim de pasi: {max(pasi_rulari)}")
print(f"Numar mediu de pasi: {sum(pasi_rulari) / len(pasi_rulari):.2f}")

# 4. Experimente pentru dimensiuni diferite
dimensiuni = [100, 1000, 5000, 10000]
medii_pasi = []

print("\n=== Experimente pentru dimensiuni diferite ===")
for n in dimensiuni:
    v, val = genereaza_date(n)
    suma_pasi = 0
    for _ in range(30):
        _, pasi = cautare_las_vegas(v, val)
        suma_pasi += pasi
    media = suma_pasi / 30
    medii_pasi.append(media)
    print(f"Dimensiune {n}: medie pasi = {media:.2f}")

# 5. Raport grafic cu matplotlib.pyplot
plt.figure(figsize=(12, 5))

# Subgrafic 1: Variatia pașilor pentru o singură dimensiune (cele 30 de rulări)
plt.subplot(1, 2, 1)
plt.plot(range(1, 31), pasi_rulari, marker='o', linestyle='', color='orange', label='Pași/rulare')
plt.axhline(y=sum(pasi_rulari) / len(pasi_rulari), color='r', linestyle='-', label='Medie')
plt.title('Variația numărului de pași (30 rulări, n=1000)')
plt.xlabel('Numărul rulării')
plt.ylabel('Pași efectuați')
plt.legend()

# Subgrafic 2: Media pașilor vs. Dimensiunea vectorului
plt.subplot(1, 2, 2)
plt.plot(dimensiuni, medii_pasi, marker='s', color='green', label='Pași medii')
plt.title('Media pașilor în funcție de dimensiunea N')
plt.xlabel('Dimensiunea vectorului (N)')
plt.ylabel('Număr mediu de pași')
plt.legend()

plt.tight_layout()
plt.savefig('grafic_las_vegas.png')
print("\nGraficul a fost salvat ca 'grafic_las_vegas.png'.")