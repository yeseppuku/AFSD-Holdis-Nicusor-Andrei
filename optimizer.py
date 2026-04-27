import json
import os

# Setări globale simple
CAMPURI_OBLIGATORII = ["nume", "cost", "profit", "categorie", "risc"]

def incarca_date(cale_fisier):
    """Citeste datele din JSON si verifica daca sunt ok."""
    if not os.path.exists(cale_fisier):
        print(f"Eroare: Nu am gasit fisierul {cale_fisier}")
        return None

    try:
        with open(cale_fisier, "r", encoding="utf-8") as f:
            date = json.load(f)
    except Exception as e:
        print(f"Eroare la citirea JSON: {e}")
        return None

    valide = []
    for i, item in enumerate(date):
        # Verificam daca are toate cheile
        if all(k in item for k in CAMPURI_OBLIGATORII):
            if isinstance(item["cost"], (int, float)) and item["cost"] > 0:
                valide.append(item)
            else:
                print(f"Sari peste {item.get('nume', i)} - cost invalid.")

    return valide

def arata_tabel(lista, mesaj="Investitii"):
    print(f"\n--- {mesaj} ---")
    print(f"{'Nr':<3} {'Nume':<15} {'Cost':>7} {'Profit':>7} {'Risc':<10}")
    for i, inv in enumerate(lista, 1):
        print(f"{i:<3} {inv['nume']:<15} {inv['cost']:>7} {inv['profit']:>7} {inv['risc']:<10}")

def statistici(date):
    print("\n=== Scurta analiza ===")
    print(f"Total optiuni: {len(date)}")
    print(f"Cel mai ieftin: {min(date, key=lambda x: x['cost'])['nume']}")
    print(f"Cel mai profitabil: {max(date, key=lambda x: x['profit'])['nume']}")

    # Categorii
    cat_count = {}
    for d in date:
        c = d['categorie']
        cat_count[c] = cat_count.get(c, 0) + 1
    print(f"Categorii detectate: {cat_count}")

def rezolva_knapsack(investitii, buget):
    """Algoritmul de programare dinamica pentru rucsac 0/1."""
    n = len(investitii)
    W = int(buget)

    # Matricea DP
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost_actual = int(investitii[i-1]['cost'])
        profit_actual = int(investitii[i-1]['profit'])
        for w in range(W + 1):
            if cost_actual <= w:
                dp[i][w] = max(dp[i-1][w], profit_actual + dp[i-1][w - cost_actual])
            else:
                dp[i][w] = dp[i-1][w]

    # Reconstructie solutie
    alese = []
    aux_w = W
    for i in range(n, 0, -1):
        if dp[i][aux_w] != dp[i-1][aux_w]:
            inv = investitii[i-1]
            alese.append(inv)
            aux_w -= int(inv['cost'])

    return alese, dp[n][W]

def main():
    cale = "investments.json"
    date = incarca_date(cale)

    if not date:
        return

    while True:
        print("\n--- MENIU ---")
        print("1. Vezi toate investitiile")
        print("2. Statistici rapide")
        print("3. Ruleaza Optimizarea (DP)")
        print("0. Iesire")

        op = input("Alege optiune: ")

        if op == "1":
            arata_tabel(date)
        elif op == "2":
            statistici(date)
        elif op == "3":
            try:
                b = float(input("Ce buget ai? "))
                rezultat, profit_max = rezolva_knapsack(date, b)

                print(f"\nREZULTAT: Profit total = {profit_max}")
                print(f"Cost total = {sum(x['cost'] for x in rezultat)}")
                arata_tabel(rezultat, "Investitii alese")
            except ValueError:
                print("Bagă un număr valid pentru buget!")
        elif op == "0":
            print("Pa!")
            break
        else:
            print("Optiune gresita.")

if __name__ == "__main__":
    main()