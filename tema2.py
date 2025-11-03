elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9, 7, 10, 4, 8]
elev_nou="Felix"
nota_elev_nou= 6
elev_de_sters="Darius"
interogari_nume=["Ana","Mara","Elena", "stop"]
absente=[1, 0, 2, 3, 0]
nota_minima=min(note)
nota_maxima=max(note)

# Partea A.

# Lista elevi si note folosing for si indici.
for i in range(len(elevi)):
    nume_elev = elevi[i]
    nota_elev = note[i]
    print(f"{nume_elev} are nota {nota_elev}")

#  Gasirea notei maxime
nota_maxima = max(note)

#  Gasirea numelor elevilor care au nota maxima
elevi_maxima = []
for i in range(len(note)):
    if note[i] == nota_maxima:
        elevi_maxima.append(elevi[i])

#  Gasirea notei minime
nota_minima = min(note)

#  Gasirea numelor elevilor care au nota minima
elevi_minima = []
for i in range(len(note)):
    if note[i] == nota_minima:
        elevi_minima.append(elevi[i])

#  Afisarea rezultatelor.
print(f"Nota cea mai mare este: {nota_maxima}")
print(f"Elevul/Elevii cu nota cea mai mare: {', '.join(elevi_maxima)}")
print("-" * 69)
print(f"Nota cea mai mica este: {nota_minima}")
print(f"Elevul/Elevii cu nota cea mai mica: {', '.join(elevi_minima)}")

# Media aritmetica a notelor

medie = sum(note) / len(note)
print(f"Media aritmetica a notelor este: {medie:.2f}")

# Afisarea elevilor cu nota mai mare sau egala cu 5.
elevi_cu_note_bune = []
for i in range(len(note)):
    if note[i] >= 5:
        elevi_cu_note_bune.append(elevi[i])
print(f"Acesti elevi au note bune: {', '.join(elevi_cu_note_bune)}")

# Partea B.
for i in range(len(note)):
    if note[i] < 10:

        print(note[i])

# Elevul predefinit

elevi.append(elev_nou)
note.append(nota_elev_nou)
print(elev_nou)
print(nota_elev_nou)

# Sterge elevul predefinit
pozitie=elevi.index("Darius")
elevi.pop(pozitie)
note.pop(pozitie)
print(elevi)

# Afiseaza din nou lista

for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")

# Partea C

# Cautari de nume cu while
i=0
print(elevi)
print(note)
print(interogari_nume)
while interogari_nume[i]!="stop":
    if interogari_nume[i] in elevi:
        j=elevi.index(interogari_nume[i])
        print(note[j])
    else:
        print("Nu exista")
    i=1+i

# Numar promovati/respinsi
respinsi=0
promovati=0
for index in range(len(note)):
    if note[i]>=5:
        promovati=promovati+1
    else:
        respinsi=respinsi+1
        print(f"{respinsi} elevii respinsi si {promovati} elevii promovati")

# Media promovatilor

lista_2=[]
for nota in note:
    if nota>=5:
        lista_2.append(nota)
print(note)
if len(lista_2)>0:
    print(sum(lista_2)/len(lista_2))