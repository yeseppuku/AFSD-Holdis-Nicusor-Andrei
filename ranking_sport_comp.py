import json


# Functia de comparare conform regulilor din cerinta
def este_mai_bun(c1, c2):
    # 1. Punctaj mai mare e mai bun
    if c1['punctaj'] > c2['punctaj']:
        return True
    if c1['punctaj'] < c2['punctaj']:
        return False

    # 2. Daca punctajul e egal, timpul mai mic e mai bun
    if c1['timp'] < c2['timp']:
        return True
    if c1['timp'] > c2['timp']:
        return False

    # 3. Daca si timpul e egal, ordonam alfabetic dupa nume
    return c1['nume'].lower() < c2['nume'].lower()


# Implementare Quicksort clasic
def quicksort_competitori(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2]
    stanga = []
    mijloc = []
    dreapta = []

    for x in lista:
        if x == pivot:
            mijloc.append(x)
        elif este_mai_bun(x, pivot):
            stanga.append(x)
        else:
            dreapta.append(x)

    return quicksort_competitori(stanga) + mijloc + quicksort_competitori(dreapta)


def incarca_date():
    try:
        with open("competitori.json", "r") as f:
            return json.load(f)
    except:
        print("Atentie: Fisierul JSON nu a fost gasit. Lista e goala.")
        return []


def salveaza_date(lista):
    with open("competitori.json", "w") as f:
        json.dump(lista, f, indent=4)


def meniu_principal():
    data = incarca_date()

    while True:
        print("\n--- SISTEM GESTIONARE CONCURS ---")
        print("1. Vezi toti competitorii")
        print("2. Adauga un om nou")
        print("3. Modifica scor/timp")
        print("4. Clasament final (Quicksort)")
        print("5. Statistici rapide")
        print("6. Salvare si Iesire")

        opt = input("Alege o optiune: ")

        if opt == "1":
            print("\nLista actuala:")
            for comp in data:
                print(f"Nume: {comp['nume']} | Punctaj: {comp['punctaj']} | Timp: {comp['timp']}")

        elif opt == "2":
            nume = input("Nume: ").strip()
            if not nume:
                print("Eroare: Numele este obligatoriu!")
                continue
            try:
                p = int(input("Punctaj: "))
                t = int(input("Timp: "))
                data.append({"nume": nume, "punctaj": p, "timp": t})
            except:
                print("Date invalide! Introdu numere intregi.")

        elif opt == "3":
            cautat = input("Introdu numele celui pe care il modifici: ")
            gasit = False
            for c in data:
                if c['nume'].lower() == cautat.lower():
                    c['punctaj'] = int(input("Punctaj nou: "))
                    c['timp'] = int(input("Timp nou: "))
                    gasit = True
                    break
            if not gasit: print("Nu l-am gasit in lista.")

        elif opt == "4":
            if not data:
                print("Nu sunt date de sortat.")
                continue

            ordonati = quicksort_competitori(data)
            print("\n--- CLASAMENT FINAL ---")
            loc = 1
            for i in range(len(ordonati)):
                # Verificam egalitatea cu cel de dinainte pentru a pune acelasi loc
                if i > 0:
                    prev = ordonati[i - 1]
                    curr = ordonati[i]
                    if not (prev['punctaj'] == curr['punctaj'] and prev['timp'] == curr['timp']):
                        loc = i + 1

                c = ordonati[i]
                print(f"Locul {loc}: {c['nume']} - {c['punctaj']} pct - {c['timp']} sec")

        elif opt == "5":
            if not data:
                print("Lipsa date.")
                continue
            pct = [x['punctaj'] for x in data]
            tmp = [x['timp'] for x in data]
            print(f"\nTotal participanti: {len(data)}")
            print(f"Cel mai mare punctaj: {max(pct)}")
            print(f"Media punctajelor: {sum(pct) / len(pct)}")
            print(f"Cel mai scurt timp: {min(tmp)}")

        elif opt == "6":
            salveaza_date(data)
            print("Date salvate. Pa!")
            break


if __name__ == "__main__":
    meniu_principal()