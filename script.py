produse = ["espresso", "latte", "cappuccino", "ceai", "ciocolata calda", "croissant"]
preturi = [8.0, 12.0, 11.0, 7.0, 10.0, 9.0]
stoc = [20, 15, 18, 30, 12, 10]
cantitati = [0, 0, 0, 0, 0, 0]
reducere_activa = 0


def afisare_produse():
    for i in range(len(produse)):
        print(f"{i}: {produse[i]} | {preturi[i]} lei | Stoc: {stoc[i]}")


def total_comanda():
    return sum(cantitati[i] * preturi[i] for i in range(len(produse)))


def reducere_stabilita(total, tip):
    if tip == "student" and total >= 30: return min(0.10 * total, total)
    if tip == "happy" and total >= 50: return min(0.15 * total, total)
    if tip == "cupon" and total >= 25: return min(7.0, total)
    print("Reducere indisponibila pentru acest total.")
    return 0


def tiparire_bon(total, reducere):
    print("\n--- BON ---")
    for i in range(len(produse)):
        if cantitati[i] > 0:
            print(f"{produse[i]}: {cantitati[i]} x {preturi[i]} = {cantitati[i] * preturi[i]} lei")
    print(f"Total: {total} | Reducere: {reducere} | Final: {total - reducere}")


while True:
    print("\n1:Meniu 2:Adauga 3:Sterge 4:Reducere 5:Final 6:Anulare 0:Iesire")
    try:
        opt = input("Optiune: ")

        if opt == "0": break

        if opt == "1":
            afisare_produse()

        elif opt == "2":
            afisare_produse()
            idx = int(input("Index produs: "))
            cant = int(input("Cantitate: "))
            if 0 <= idx < len(produse) and cant > 0 and (cantitati[idx] + cant) <= stoc[idx]:
                cantitati[idx] += cant
            else:
                print("Eroare: Stoc insuficient sau index invalid.")

        elif opt == "3":
            idx = int(input("Index produs: "))
            cant = int(input("Cantitate de scazut: "))
            if 0 <= idx < len(produse) and 0 < cant <= cantitati[idx]:
                cantitati[idx] -= cant
            else:
                print("Eroare: Cantitate invalida.")

        elif opt == "4":
            suma = total_comanda()
            if suma == 0:
                print("Comanda este goala.")
            else:
                tip = input("Alege (student/happy/cupon/fara/inapoi): ")
                if tip == "fara":
                    reducere_activa = 0
                elif tip != "inapoi":
                    reducere_activa = reducere_stabilita(suma, tip)

        elif opt == "5":
            suma = total_comanda()
            if suma > 0:
                tiparire_bon(suma, reducere_activa)
                for i in range(len(produse)):
                    stoc[i] -= cantitati[i]
                    cantitati[i] = 0
                reducere_activa = 0
            else:
                print("Esti sarac? N-ai adaugat nimic :))).")

        elif opt == "6":
            cantitati = [0] * len(produse)
            reducere_activa = 0
            print("Comanda a fost anulata.")
        else:
            print("Optiune invalida.")

    except ValueError:
        print("Eroare: Nu faci diferenta dintre litere si numere? sad...")