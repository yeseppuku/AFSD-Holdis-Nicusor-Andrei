import random
import matplotlib.pyplot as plt

# 1. Modelarea jocului
def runda_joc():
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    suma = zar1 + zar2
    return suma == 7 or suma == 11

# 2. Simularea Monte Carlo
def simulare_monte_carlo(N):
    castiguri = 0
    for _ in range(N):
        if runda_joc():
            castiguri += 1
    return castiguri / N

# 3. Experimente repetate
valori_N = [100, 1000, 10000, 100000]
estimari = []

print("=== Experimente Monte Carlo ===")
for N in valori_N:
    prob_estimata = simulare_monte_carlo(N)
    estimari.append(prob_estimata)
    print(f"Pentru N = {N}, probabilitatea estimata este: {prob_estimata:.4f}")

# Demonstrăm variația pentru același N
N_fix = 1000
rulari_independente = 10
print(f"\n10 rulari independente pentru N = {N_fix}:")
for i in range(rulari_independente):
    print(f"Rularea {i+1}: {simulare_monte_carlo(N_fix):.4f}")

# 4. Raport grafic cu matplotlib.pyplot
plt.figure(figsize=(10, 6))
# Folosim log scale pentru axa X pentru o vizualizare mai buna a diferentelor de magnitudine
plt.plot(valori_N, estimari, marker='o', linestyle='-', color='b', label='Probabilitate Estimată')
plt.axhline(y=8/36, color='r', linestyle='--', label='Probabilitate Teoretică (~0.222)')

plt.xscale('log')
plt.title('Evoluția probabilității estimate cu creșterea numărului de simulări (N)')
plt.xlabel('Numărul de simulări (N) - Scală logaritmică')
plt.ylabel('Probabilitate estimată')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)

plt.savefig('grafic_monte_carlo.png')
print("\nGraficul a fost salvat ca 'grafic_monte_carlo.png'.")