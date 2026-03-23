import csv
import json
import os


# --- 1. Citire Produse din CSV ---
def citeste_produse_csv(fisier):
    produse = {}
    try:
        with open(fisier, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Conversie ID în string pentru a fi cheie în dicționar conform cerinței
                produse[str(row['id'])] = {
                    "nume": row['nume'],
                    "pret": float(row['pret']),
                    "stoc": int(row['stoc'])
                }
    except FileNotFoundError:
        print(f"Eroare: Fișierul {fisier} nu există!")
    return produse


# --- 2. Citire Reduceri din JSON ---
def citeste_reduceri_json(fisier):
    try:
        with open(fisier, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Eroare: Fișierul {fisier} nu există!")
        return {}


# --- 3. Afișare Meniu ---
def afiseaza_meniu(produse):
    print("\n" + "=" * 40)
    print(f"{'ID':<5} {'Produs':<18} {'Pret':<10} {'Stoc':<5}")
    print("-" * 40)
    for id_p, info in produse.items():
        print(f"{id_p:<5} {info['nume']:<18} {info['pret']:>5.2f} lei {info['stoc']:>5} buc")
    print("=" * 40)


# --- 4. Adăugare Produs ---
def adauga_produs(comanda, produse, id_produs, cantitate):
    id_s = str(id_produs)
    if id_s not in produse:
        print(" Eroare: ID-ul produsului nu există.")
        return

    # Calculăm stocul disponibil (stoc total - ce e deja în coș)
    stoc_disponibil = produse[id_s]['stoc'] - comanda.get(id_s, 0)

    if cantitate <= 0:
        print(" Eroare: Cantitatea trebuie să fie minim 1.")
    elif cantitate > stoc_disponibil:
        print(f" Eroare: Stoc insuficient! Mai poți adăuga doar {stoc_disponibil} unități.")
    else:
        comanda[id_s] = comanda.get(id_s, 0) + cantitate
        print(f" Succes: {cantitate} x {produse[id_s]['nume']} adăugat în comandă.")


# --- 5. Scădere/Eliminare Produs ---
def scade_produs(comanda, id_produs, cantitate):
    id_s = str(id_produs)
    if id_s not in comanda:
        print(" Eroare: Produsul nu se află în comanda curentă.")
        return

    if cantitate <= 0:
        print(" Eroare: Cantitatea de scăzut trebuie să fie pozitivă.")
    elif cantitate >= comanda[id_s]:
        del comanda[id_s]
        print(" Produsul a fost eliminat complet din comandă.")
    else:
        comanda[id_s] -= cantitate
        print(f" S-au scăzut {cantitate} unități.")


# --- 6. Calcul Total ---
def calculeaza_total(comanda, produse):
    total = 0.0
    for id_p, cantitate in comanda.items():
        total += produse[id_p]['pret'] * cantitate
    return total


# --- 7. Calcul Reducere ---
def calculeaza_reducere(total, tip_reducere, reduceri):
    if not tip_reducere or tip_reducere not in reduceri:
        return 0.0

    regula = reduceri[tip_reducere]
    if total < regula['prag']:
        print(f" Atenție: Reducerea '{tip_reducere}' necesită un total de minim {regula['prag']} lei.")
        return 0.0

    if regula['tip'] == "procent":
        return total * (regula['valoare'] / 100)
    elif regula['tip'] == "fix":
        return float(regula['valoare'])
    return 0.0


# --- 8. Generare Bon ---
def genereaza_bon(comanda, produse, total, reducere):
    bon = "\n" + "*" * 30 + "\n"
    bon += "      BON FISCAL CAFE      \n"
    bon += "*" * 30 + "\n"
    for id_p, cant in comanda.items():
        p = produse[id_p]
        subtotal = p['pret'] * cant
        bon += f"{p['nume'][:15]:<15} {cant}x{p['pret']:.2f} = {subtotal:.2f}\n"

    bon += "-" * 30 + "\n"
    bon += f"SUBTOTAL:           {total:.2f} lei\n"
    bon += f"REDUCERE:          -{reducere:.2f} lei\n"
    bon += f"TOTAL FINAL:        {total - reducere:.2f} lei\n"
    bon += "*" * 30 + "\n"
    return bon


# --- 9. Scriere Bon TXT ---
def scrie_bon_txt(fisier, text_bon):
    with open(fisier, 'w', encoding='utf-8') as f:
        f.write(text_bon)


# --- 10. Golește Comanda ---
def goleste_comanda(comanda):
    comanda.clear()


# --- Bucla Principală ---
def main():
    produse = citeste_produse_csv('produse.csv')
    reduceri = citeste_reduceri_json('reduceri.json')
    comanda = {}
    reducere_curenta = ""

    while True:
        print("\n--- SISTEM GESTIUNE CAFENEA ---")
        print("1 - Afisare meniu produse")
        print("2 - Adaugare produs in comanda")
        print("3 - Scadere/eliminare produs")
        print("4 - Aplicare reducere")
        print("5 - Finalizare comanda")
        print("6 - Anulare comanda")
        print("0 - Iesire")

        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            afiseaza_meniu(produse)

        elif optiune == "2":
            id_p = input("Introdu ID-ul produsului: ")
            try:
                cant = int(input("Introdu cantitatea: "))
                adauga_produs(comanda, produse, id_p, cant)
            except ValueError:
                print("Eroare: Introdu un număr întreg!")

        elif optiune == "3":
            id_p = input("Introdu ID-ul de eliminat/scăzut: ")
            try:
                cant = int(input("Introdu cantitatea de scăzut: "))
                scade_produs(comanda, id_p, cant)
            except ValueError:
                print("Eroare: Introdu un număr întreg!")

        elif optiune == "4":
            total_curent = calculeaza_total(comanda, produse)
            if total_curent == 0:
                print("Comanda este goală! Nu poți aplica reduceri.")
                continue

            print("\nReduceri disponibile:")
            for i, nume_red in enumerate(reduceri.keys(), 1):
                print(f"{i} - {nume_red}")
            print("4 - fara reducere\n0 - inapoi")

            opt_red = input("Alege: ")
            mapping = {"1": "student", "2": "happy", "3": "cupon", "4": ""}
            if opt_red in mapping:
                reducere_curenta = mapping[opt_red]
                print(f"Reducere selectată: {reducere_curenta if reducere_curenta else 'Niciuna'}")

        elif optiune == "5":
            if not comanda:
                print("Eroare: Nu poți finaliza o comandă fără produse.")
                continue

            total = calculeaza_total(comanda, produse)
            valoare_red = calculeaza_reducere(total, reducere_curenta, reduceri)

            bon_text = genereaza_bon(comanda, produse, total, valoare_red)
            print(bon_text)
            scrie_bon_txt("bon.txt", bon_text)

            # Actualizare stoc în memorie
            for id_p, cant in comanda.items():
                produse[id_p]['stoc'] -= cant

            goleste_comanda(comanda)
            reducere_curenta = ""
            print("Comandă finalizată! Bonul a fost generat (bon.txt).")

        elif optiune == "6":
            goleste_comanda(comanda)
            reducere_curenta = ""
            print("Comanda a fost anulată.")

        elif optiune == "0":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă!")


if __name__ == "__main__":
    main()