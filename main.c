#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int cifre[400];
    int lg;
} NumarMare;

// Funcție utilitară pentru a converti string în structura NumarMare
NumarMare stringToNumar(char s[]) {
    NumarMare n;
    n.lg = strlen(s);
    for (int i = 0; i < n.lg; i++) {
        n.cifre[i + 1] = s[n.lg - 1 - i] - '0';
    }
    return n;
}

// Funcție utilitară pentru afișare
void afiseaza(NumarMare n) {
    for (int i = n.lg; i >= 1; i--) {
        printf("%d", n.cifre[i]);
    }
    printf("\n");
}

// 1. Funcția de Adunare
NumarMare adunare(NumarMare a, NumarMare b) {
    NumarMare rez;
    int i, t = 0;
    rez.lg = (a.lg > b.lg) ? a.lg : b.lg;

    // Completăm cu zero vectorul mai scurt pentru siguranță
    for (i = a.lg + 1; i <= rez.lg + 1; i++) a.cifre[i] = 0;
    for (i = b.lg + 1; i <= rez.lg + 1; i++) b.cifre[i] = 0;

    for (i = 1; i <= rez.lg; i++) {
        int suma = a.cifre[i] + b.cifre[i] + t;
        rez.cifre[i] = suma % 10;
        t = suma / 10;
    }

    if (t) {
        rez.lg++;
        rez.cifre[rez.lg] = t;
    }
    return rez;
}

// 2. Funcția de Scădere (presupunem a >= b)
NumarMare scadere(NumarMare a, NumarMare b) {
    NumarMare rez;
    int i, t = 0;
    rez.lg = a.lg;

    for (i = b.lg + 1; i <= a.lg; i++) b.cifre[i] = 0;

    for (i = 1; i <= rez.lg; i++) {
        int sub = a.cifre[i] - b.cifre[i] - t;
        if (sub < 0) {
            sub += 10;
            t = 1;
        }
        else {
            t = 0;
        }
        rez.cifre[i] = sub;
    }

    // Eliminăm zerourile nesemnificative de la final (ex: 100 - 95 = 005 -> 5)
    while (rez.lg > 1 && rez.cifre[rez.lg] == 0) rez.lg--;

    return rez;
}

// 3. Funcția de Înmulțire cu o cifră
NumarMare inmultireCifra(NumarMare a, int cifra) {
    NumarMare rez;
    if (cifra == 0) {
        rez.lg = 1; rez.cifre[1] = 0;
        return rez;
    }

    int i, t = 0;
    rez.lg = a.lg;

    for (i = 1; i <= rez.lg; i++) {
        int prod = a.cifre[i] * cifra + t;
        rez.cifre[i] = prod % 10;
        t = prod / 10;
    }

    while (t) {
        rez.lg++;
        rez.cifre[rez.lg] = t % 10;
        t /= 10;
    }
    return rez;
}

int main() {
    char s1[200], s2[200];
    int cifra;

    printf("Primul numar: "); scanf("%s", s1);
    printf("Al doilea numar: "); scanf("%s", s2);
    printf("O cifra pentru inmultire: "); scanf("%d", &cifra);

    NumarMare n1 = stringToNumar(s1);
    NumarMare n2 = stringToNumar(s2);

    // Adunare
    printf("\nSuma: ");
    afiseaza(adunare(n1, n2));

    // Scădere (Verificăm care e mai mare)
    printf("Diferenta (Mare - Mic): ");
    if (n1.lg > n2.lg || (n1.lg == n2.lg && strcmp(s1, s2) >= 0)) {
        afiseaza(scadere(n1, n2));
    }
    else {
        afiseaza(scadere(n2, n1));
    }

    // Înmulțire
    printf("Produsul primului numar cu %d: ", cifra);
    afiseaza(inmultireCifra(n1, cifra));

    return 0;
}