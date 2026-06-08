import json
import os

CAMPURI_OBLIGATORII = ["nume", "cost", "profit", "categorie", "risc"]

def incarca_date(cale_fisier):
    """Citeste datele din JSON si verifica daca sunt valide conform cerintelor."""
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
    if not isinstance(date, list):
        print("Eroare: Structura JSON-ului trebuie sa fie o lista de obiecte.")
        return None

    for i, item in enumerate(date):
        if all(k in item for k in CAMPURI_OBLIGATORII):
            if isinstance(item["cost"], (int, float)) and item["cost"] > 0 and isinstance(item["profit"], (int, float)) and item["profit"] > 0:
                valide.append(item)
            else:
                print(f"Sari peste elementul {item.get('nume', i)} - valori numerice invalide.")
        else:
            print(f"Sari peste elementul index {i} - campuri obligatorii lipsa.")

    return valide


def arata_tabel(lista, mesaj="Investitii"):
    """Afiseaza datele intr-un format lizibil si ordonat (Tabel)."""
    if not lista:
        print(f"\n--- {mesaj} (Lista este vida) ---")
        return
    print(f"\n--- {mesaj} ---")
    print(f"{'Nr':<3} | {'Nume':<15} | {'Cost':>7} | {'Profit':>7} | {'Raport P/C':>10} | {'Categorie':<12} | {'Risc':<8}")
    print("-" * 75)
    for i, inv in enumerate(lista, 1):
        raport = inv['profit'] / inv['cost']
        print(f"{i:<3} | {inv['nume']:<15} | {inv['cost']:>7} | {inv['profit']:>7} | {raport:>10.3f} | {inv['categorie']:<12} | {inv['risc']:<8}")


def statistici(date):
    """Analiza descriptiva ceruta la punctul 3."""
    if not date:
        return
    print("\n" + "="*10 + " ANALIZA DESCRIPTIVA " + "="*10)
    print(f"Numar total de investitii disponibile: {len(date)}")
    print(f"Investitia cu costul minim: {min(date, key=lambda x: x['cost'])['nume']} ({min(date, key=lambda x: x['cost'])['cost']})")
    print(f"Investitia cu costul maxim: {max(date, key=lambda x: x['cost'])['nume']} ({max(date, key=lambda x: x['cost'])['cost']})")
    print(f"Investitia cu profitul maxim: {max(date, key=lambda x: x['profit'])['nume']} ({max(date, key=lambda x: x['profit'])['profit']})")

    # Distributii
    cat_count = {}
    risc_count = {}
    for d in date:
        cat_count[d['categorie']] = cat_count.get(d['categorie'], 0) + 1
        risc_count[d['risc']] = risc_count.get(d['risc'], 0) + 1
        
    print(f"Distributie pe categorii: {cat_count}")
    print(f"Distributie pe niveluri de risc: {risc_count}")


# --- CERINTA 4: FILTRARE SI ORDONARE ---
def meniu_filtrare_ordonare(date):
    date_lucru = date.copy()
    while True:
        print("\n--- Submeniu: Filtrare si Ordonare ---")
        print("1. Filtrare dupa Categorie")
        print("2. Filtrare dupa Nivel de Risc")
        print("3. Ordonare dupa Cost")
        print("4. Ordonare dupa Profit")
        print("5. Ordonare dupa Raport Profit/Cost")
        print("6. Reseteaza filtrele (Inapoi la lista initiala)")
        print("0. Inapoi la meniul principal")
        
        op = input("Alege optiune: ")
        if op == "1":
            cat = input("Introdu categoria dorita: ").strip()
            date_lucru = [x for x in date_lucru if x['categorie'].lower() == cat.lower()]
            arata_tabel(date_lucru, f"Filtrare categorie: {cat}")
        elif op == "2":
            risc = input("Introdu riscul dorita (scazut/mediu/ridicat): ").strip()
            date_lucru = [x for x in date_lucru if x['risc'].lower() == risc.lower()]
            arata_tabel(date_lucru, f"Filtrare risc: {risc}")
        elif op == "3":
            date_lucru.sort(key=lambda x: x['cost'])
            arata_tabel(date_lucru, "Ordonat crescator dupa Cost")
        elif op == "4":
            date_lucru.sort(key=lambda x: x['profit'], reverse=True)
            arata_tabel(date_lucru, "Ordonat descrescator dupa Profit")
        elif op == "5":
            date_lucru.sort(key=lambda x: x['profit']/x['cost'], reverse=True)
            arata_tabel(date_lucru, "Ordonat descrescator dupa Raport Profit/Cost")
        elif op == "6":
            date_lucru = date.copy()
            arata_tabel(date_lucru, "Lista a fost resetata la starea initiala")
        elif op == "0":
            break
        else:
            print("Optiune invalida.")


# --- CERINTA 6 & 7: PROGRAMARE DINAMICA SI AFISARE MATRICE ---
def afiseaza_matrice_dp(dp, investitii, max_col=15):
    """Afiseaza tabelul de programare dinamica partial sau complet."""
    print("\n--- TABELUL DE PROGRAMARE DINAMICA (DP) ---")
    W = len(dp[0]) - 1
    limita_coloane = min(W + 1, max_col)
    
    header = f"{'Item':<15} | " + " ".join(f"{w:>4}" for w in range(limita_coloane))
    if W + 1 > max_col:
        header += " ..."
    print(header)
    print("-" * len(header))
    
    for i in range(len(dp)):
        nume_linie = "Baza (0)" if i == 0 else investitii[i-1]['nume']
        linie = f"{nume_linie:<15} | " + " ".join(f"{dp[i][w]:>4}" for w in range(limita_coloane))
        if W + 1 > max_col:
            linie += " ..."
        print(linie)
    print("> Nota: Valorile reprezinta profitul maxim asociat subbugetelor.")


def rezolva_knapsack(investitii, buget, exclude_risc_ridicat=False):
    """Algoritmul DP Rucsac 0/1 cu reconstructie si managementul restrictiilor."""
    # Aplicam restrictia suplimentara daca este activa
    if exclude_risc_ridicat:
        investitii_filtrate = [x for x in investitii if x['risc'].lower() != "ridicat"]
    else:
        investitii_filtrate = investitii.copy()

    n = len(investitii_filtrate)
    W = int(buget)

    # Alocare tabela DP
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Completare tabel
    for i in range(1, n + 1):
        cost_actual = int(investitii_filtrate[i-1]['cost'])
        profit_actual = int(investitii_filtrate[i-1]['profit'])
        for w in range(W + 1):
            if cost_actual <= w:
                dp[i][w] = max(dp[i-1][w], profit_actual + dp[i-1][w - cost_actual])
            else:
                dp[i][w] = dp[i-1][w]

    # Reconstructie
    alese = []
    aux_w = W
    for i in range(n, 0, -1):
        if dp[i][aux_w] != dp[i-1][aux_w]:
            inv = investitii_filtrate[i-1]
            alese.append(inv)
            aux_w -= int(inv['cost'])

    return alese, dp[n][W], dp, investitii_filtrate


# --- MENIUL PRINCIPAL ---
def main():
    # Poti schimba numele fisierului JSON aici
    cale = "investments.json"
    
    # Generam un fisier mock direct daca nu exista, pentru a nu crapa codul la rulare
    if not os.path.exists(cale):
        mock_data = [
            {"nume": "Actiuni_A", "cost": 4000, "profit": 1200, "categorie": "actiuni", "risc": "mediu"},
            {"nume": "Fond_B", "cost": 2500, "profit": 700, "categorie": "fonduri", "risc": "scazut"},
            {"nume": "Startup_C", "cost": 5000, "profit": 2000, "categorie": "startup", "risc": "ridicat"},
            {"nume": "ETF_D", "cost": 3000, "profit": 850, "categorie": "etf", "risc": "mediu"}
        ]
        with open(cale, "w", encoding="utf-8") as f:
            json.dump(mock_data, f, indent=2)

    date = incarca_date(cale)
    if not date:
        print("Aplicatia nu poate porni fara date valide.")
        return

    while True:
        print("\n" + "="*15 + " MENIU PRINCIPAL " + "="*15)
        print("1. Vizualizare portofoliu investitii")
        print("2. Analiza descriptiva (Statistici)")
        print("3. Filtrare si Ordonare date")
        print("4. Executa Optimizare (Programare Dinamica)")
        print("0. Iesire")

        op = input("Alege optiunea: ")

        if op == "1":
            arata_tabel(date, "Toate Investitiile Disponibile")
        elif op == "2":
            statistici(date)
        elif op == "3":
            meniu_filtrare_ordonare(date)
        elif op == "4":
            try:
                buget_input = float(input("\nIntroduceti bugetul maxim disponibil (valoare pozitiva): "))
                if buget_input <= 0:
                    print("Eroare: Bugetul trebuie sa fie strict mai mare decat 0!")
                    continue
                
                print("\nDoriti activarea Restricției Suplimentare?")
                print("1. Nu (Optimizare standard)")
                print("2. Da (Exclude complet investitiile cu risc 'ridicat')")
                alegere_restrictie = input("Alegere: ")
                
                aplică_restricție = (alegere_restrictie == "2")
                
                # Rulam algoritmul
                rezultat, profit_max, tabela_dp, inv_folosite = rezolva_knapsack(date, buget_input, aplică_restricție)
                
                # Cerinta 7: Afisarea tabelului DP (afisam primele 20 de coloane ca sa nu satureze consola)
                afiseaza_matrice_dp(tabela_dp, inv_folosite, max_col=20)
                
                # Calculare metrici finale cerute
                cost_total = sum(x['cost'] for x in rezultat)
                buget_ramas = buget_input - cost_total
                
                # Cerinta 9 & 10: Afisarea rezultatului final complet conform structurii cerute
                print("\n" + "*"*10 + " REZULTAT FINAL OPTIMIZARE " + "*"*10)
                print(f"Buget disponibil:      {buget_input}")
                print(f"Profit optim obtinut:  {profit_max}")
                print(f"Cost total utilizat:   {cost_total}")
                print(f"Buget ramas neutilizat: {buget_ramas}")
                
                arata_tabel(rezultat, "Portofoliu de Investitii Selectate")
                
            except ValueError:
                print("Eroare: Va rugam sa introduceti un numar valid pentru buget.")
        elif op == "0":
            print("Aplicatie inchisa. Succes!")
            break
        else:
            print("Optiune invalida.")

if __name__ == "__main__":
    main()
