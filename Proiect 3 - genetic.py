import random
import matplotlib.pyplot as plt

# 1. Definirea problemei
candidati = [
    {"nume": "Alice", "cost": 300, "scor": 85},
    {"nume": "Bob", "cost": 450, "scor": 90},
    {"nume": "Charlie", "cost": 200, "scor": 60},
    {"nume": "Diana", "cost": 500, "scor": 95},
    {"nume": "Eve", "cost": 150, "scor": 40},
    {"nume": "Frank", "cost": 350, "scor": 75},
    {"nume": "Grace", "cost": 400, "scor": 80},
    {"nume": "Heidi", "cost": 250, "scor": 70},
    {"nume": "Ivan", "cost": 600, "scor": 98},
    {"nume": "Judy", "cost": 100, "scor": 30}
]
BUGET_MAXIM = 1500


# 2. Reprezentarea unei soluții (Ex: [1, 0, 1, 0, 0, 1, 1, 0, 0, 0])

# 3. Funcția de fitness
def calculeaza_fitness(cromozom):
    cost_total = 0
    scor_total = 0
    for i in range(len(cromozom)):
        if cromozom[i] == 1:
            cost_total += candidati[i]["cost"]
            scor_total += candidati[i]["scor"]

    # Penalizare: daca depasim bugetul, solutia este invalida (fitness 0)
    if cost_total > BUGET_MAXIM:
        return 0, cost_total, scor_total
    return scor_total, cost_total, scor_total


# 4. Populația inițială
def genereaza_populatie(dimensiune):
    populatie = []
    for _ in range(dimensiune):
        cromozom = [random.choice([0, 1]) for _ in range(len(candidati))]
        populatie.append(cromozom)
    return populatie


# 5. Operatorii genetici
def selectie_turneu(populatie, k=3):
    participanti = random.sample(populatie, k)
    cel_mai_bun = max(participanti, key=lambda c: calculeaza_fitness(c)[0])
    return cel_mai_bun


def crossover(parinte1, parinte2):
    punct = random.randint(1, len(parinte1) - 1)
    copil1 = parinte1[:punct] + parinte2[punct:]
    copil2 = parinte2[:punct] + parinte1[punct:]
    return copil1, copil2


def mutatie(cromozom, rata_mutatie=0.1):
    for i in range(len(cromozom)):
        if random.random() < rata_mutatie:
            cromozom[i] = 1 - cromozom[i]  # Inversare bit
    return cromozom


# 6. Rularea pe mai multe generații
NUMAR_GENERATII = 50
DIMENSIUNE_POPULATIE = 20

populatie = genereaza_populatie(DIMENSIUNE_POPULATIE)
istoric_fitness = []
cel_mai_bun_global = None
max_fitness_global = -1

print("=== Algoritm Genetic: Selectia Echipei ===")
for generatie in range(NUMAR_GENERATII):
    # Evaluare
    fitness_populatie = [calculeaza_fitness(c)[0] for c in populatie]
    max_fitness_curent = max(fitness_populatie)
    istoric_fitness.append(max_fitness_curent)

    # Salvare cel mai bun global
    pentru_index = fitness_populatie.index(max_fitness_curent)
    if max_fitness_curent > max_fitness_global:
        max_fitness_global = max_fitness_curent
        cel_mai_bun_global = populatie[pentru_index]

    # Generare noua populatie
    populatie_noua = []
    # Elitism: pastram cel mai bun cromozom
    populatie_noua.append(cel_mai_bun_global)

    while len(populatie_noua) < DIMENSIUNE_POPULATIE:
        p1 = selectie_turneu(populatie)
        p2 = selectie_turneu(populatie)
        c1, c2 = crossover(p1, p2)
        populatie_noua.append(mutatie(c1))
        if len(populatie_noua) < DIMENSIUNE_POPULATIE:
            populatie_noua.append(mutatie(c2))

    populatie = populatie_noua

# Afisare rezultate finale
fit, cost, scor = calculeaza_fitness(cel_mai_bun_global)
print("\nCea mai buna echipa gasita:")
echipa_nume = [candidati[i]["nume"] for i in range(len(cel_mai_bun_global)) if cel_mai_bun_global[i] == 1]
print(f"Membri: {', '.join(echipa_nume)}")
print(f"Scor total: {scor}")
print(f"Cost total: {cost} (Buget maxim: {BUGET_MAXIM})")

# 7. Raport grafic cu matplotlib.pyplot
plt.figure(figsize=(10, 6))
plt.plot(range(NUMAR_GENERATII), istoric_fitness, marker='.', color='purple', label='Cel mai bun Fitness')
plt.title('Evoluția celui mai bun fitness pe parcursul generațiilor')
plt.xlabel('Generația')
plt.ylabel('Fitness (Scor total valid)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('grafic_genetic.png')
print("\nGraficul a fost salvat ca 'grafic_genetic.png'.")