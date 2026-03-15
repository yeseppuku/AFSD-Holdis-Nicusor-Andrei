import csv
import os


# --- Functiile care fac treaba (Logica) ---

def adauga_termen(glosar):
    """ Cere un cuvant nou si il pune in dictionar daca nu exista deja. """
    termen = input("Ce cuvant vrei sa adaugi? ").strip().lower()

    if termen in glosar:
        print("Hopa! Acest cuvant este deja in lista.")
        return

    definitie = input("Ce inseamna? ")
    categorie = input("Din ce categorie face parte? ")
    exemplu = input("Da-mi un exemplu de folosire: ")

    glosar[termen] = {
        "definitie": definitie,
        "categorie": categorie,
        "exemplu": exemplu
    }
    print("Gata! L-am adaugat.")


def cautare_exacta(glosar):
    """ Cauta cuvantul intreg si arata detaliile. """
    termen = input("Ce cuvant cauti? ").strip().lower()
    if termen in glosar:
        info = glosar[termen]
        print(f"\nAm gasit: {termen.upper()}")
        print(f"- Inseamna: {info['definitie']}")
        print(f"- Categorie: {info['categorie']}")
        print(f"- Exemplu: {info['exemplu']}")
    else:
        print("Nu am gasit acest cuvant exact.")


def cautare_fragment(glosar):
    """ Cauta cuvinte care contin o anumita bucata de text. """
    fragment = input("Scrie o parte din cuvant: ").strip().lower()
    gasite = [t for t in glosar if fragment in t]

    if gasite:
        print(f"Am gasit aceste variante: {', '.join(gasite)}")
    else:
        print("Nu am gasit nimic care sa semene.")


def actualizeaza_termen(glosar):
    """ Schimba informatia pentru un cuvant care exista deja. """
    termen = input("Ce cuvant vrei sa modifici? ").strip().lower()
    if termen not in glosar:
        print("Acest cuvant nu exista in glosar.")
        return

    print("Ce vrei sa schimbi? (definitie / categorie / exemplu)")
    alegere = input("Scrie alegerea: ").strip().lower()

    if alegere in glosar[termen]:
        noua_valoare = input(f"Scrie noua varianta pentru {alegere}: ")
        glosar[termen][alegere] = noua_valoare
        print("S-a rezolvat! Am actualizat informatia.")
    else:
        print("Nu am inteles ce vrei sa schimbi.")


def sterge_termen(glosar):
    """ Elimina cuvantul din dictionar. """
    termen = input("Ce cuvant vrei sa stergi? ").strip().lower()
    if termen in glosar:
        del glosar[termen]
        print(f"Cuvantul '{termen}' a fost sters.")
    else:
        print("Nu pot sterge ceva ce nu exista.")


def afiseaza_glosar(glosar):
    """ Arata tot ce avem in lista. """
    if not glosar:
        print("Glosarul este gol.")
        return
    print("\n=== GLOSAR COMPLET ===")
    for t, info in glosar.items():
        print(f"* {t.upper()} | Cat: {info['categorie']} | Def: {info['definitie']}")


def afiseaza_statistici(glosar):
    """ Arata cate cuvinte avem in total si pe categorii. """
    if not glosar:
        print("Glosarul e gol.")
        return

    print(f"\nTotal termeni: {len(glosar)}")
    numaratoare = {}
    for info in glosar.values():
        cat = info['categorie']
        numaratoare[cat] = numaratoare.get(cat, 0) + 1

    for cat, total in numaratoare.items():
        print(f"- {cat}: {total} cuvinte")


def salveaza_csv(glosar):
    """ Pune totul in fisierul glosar.csv. """
    try:
        with open("glosar.csv", 'w', newline='', encoding='utf-8') as f:
            scriitor = csv.writer(f)
            scriitor.writerow(["termen", "definitie", "categorie", "exemplu"])
            for t, info in glosar.items():
                scriitor.writerow([t, info['definitie'], info['categorie'], info['exemplu']])
        print("Salvat cu succes in glosar.csv!")
    except:
        print("Eroare la salvare.")


def incarca_csv(glosar):
    """ Aduce datele din fisierul glosar.csv in program. """
    if not os.path.exists("glosar.csv"):
        print("Nu am gasit fisierul glosar.csv.")
        return

    glosar.clear()
    with open("glosar.csv", 'r', encoding='utf-8') as f:
        cititor = csv.DictReader(f)
        for rand in cititor:
            glosar[rand['termen']] = {
                "definitie": rand['definitie'],
                "categorie": rand['categorie'],
                "exemplu": rand['exemplu']
            }
    print("Datele au fost incarcate!")


# --- MENIUL INTERACTIV ---

def meniu_principal():
    glosar = {}  # Aici tinem datele cat timp ruleaza programul

    while True:
        print("\n" + "=" * 30)
        print("      MENIU INTERACTIV")
        print("=" * 30)
        print("1. Adauga termen")
        print("2. Cauta exact")
        print("3. Cauta fragment")
        print("4. Modifica termen")
        print("5. Sterge termen")
        print("6. Vezi tot glosarul")
        print("7. Statistici")
        print("8. Salveaza in CSV")
        print("9. Incarca din CSV")
        print("0. Iesire")
        print("=" * 30)

        optiune = input("Alege o cifra (0-9): ").strip()

        if optiune == "1":
            adauga_termen(glosar)
        elif optiune == "2":
            cautare_exacta(glosar)
        elif optiune == "3":
            cautare_fragment(glosar)
        elif optiune == "4":
            actualizeaza_termen(glosar)
        elif optiune == "5":
            sterge_termen(glosar)
        elif optiune == "6":
            afiseaza_glosar(glosar)
        elif optiune == "7":
            afiseaza_statistici(glosar)
        elif optiune == "8":
            salveaza_csv(glosar)
        elif optiune == "9":
            incarca_csv(glosar)
        elif optiune == "0":
            print("Inchidem programul... La revedere!")
            break
        else:
            print("Optiune gresita! Incearca din nou.")


# linia de start cod:
if __name__ == "__main__":
    meniu_principal()