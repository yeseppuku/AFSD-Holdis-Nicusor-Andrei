#include <stdio.h>

int main() {
    int optiune;
    int valid;

    do {
        printf("\n====================================");
        printf("\n          MENIU INTERACTIV          ");
        printf("\n====================================");
        printf("\n1. Maximul si frecventa acestuia");
        printf("\n2. CMMDC si CMMMC");
        printf("\n3. Conversie in baza b (b < 10)");
        printf("\n4. Primele n numere Fibonacci");
        printf("\n5. Iesire");
        printf("\n====================================");
        printf("\nAlegeti o optiune (1-5): ");

        // Citim si verificam daca s-a introdus un numar valid
        // scanf returneaza numarul de elemente citite cu succes (1 in cazul nostru)
        valid = scanf("%d", &optiune);

        if (valid != 1) {
            printf("\n!!! EROARE: Ati introdus un caracter nevalid. Va rugam introduceti o cifra intre 1 si 5.\n");

            // CURATARE BUFFER: Citim caracterele ramase in buffer pana la 'newline' (\n)
            // Fara asta, programul ar intra intr-o bucla infinita
            while (getchar() != '\n');

            optiune = 0; // Resetam optiunea pentru a forța reafișarea meniului
            continue;    // Revenim la inceputul buclei do-while
        }

        switch (optiune) {
        case 1: {
            int n, i, numar, max, frecventa = 0;
            printf("Cati termeni are sirul (n)? ");
            scanf("%d", &n);
            if (n <= 0) {
                printf("Eroare: n trebuie sa fie > 0!\n");
            }
            else {
                printf("Introduceti numerele:\n");
                for (i = 0; i < n; i++) {
                    scanf("%d", &numar);
                    if (i == 0) { max = numar; frecventa = 1; }
                    else if (numar > max) { max = numar; frecventa = 1; }
                    else if (numar == max) { frecventa++; }
                }
                printf("Maxim: %d, Aparitii: %d\n", max, frecventa);
            }
            break;
        }

        case 2: {
            int a, b, m_orig, n_orig, r;
            printf("Introduceti m si n: ");
            scanf("%d %d", &m_orig, &n_orig);
            a = m_orig; b = n_orig;
            while (b != 0) { r = a % b; a = b; b = r; }
            int cmmdc = a;
            long long cmmmc = (long long)m_orig * n_orig / cmmdc;
            printf("CMMDC = %d, CMMMC = %lld\n", cmmdc, cmmmc);
            break;
        }

        case 3: {
            int n_num, b, rest;
            long long rezultat = 0, p = 1;
            printf("Introduceti n si baza b (<10): ");
            scanf("%d %d", &n_num, &b);
            int copie = n_num;
            if (n_num == 0) printf("Rezultat: 0\n");
            else {
                while (copie > 0) {
                    rest = copie % b;
                    rezultat += (long long)rest * p;
                    p *= 10;
                    copie /= b;
                }
                printf("Rezultat: %lld\n", rezultat);
            }
            break;
        }

        case 4: {
            int n_fib, f1 = 0, f2 = 1, f3, i;
            printf("Cati termeni Fibonacci? ");
            scanf("%d", &n_fib);
            for (i = 1; i <= n_fib; i++) {
                if (i == 1) printf("%d ", f1);
                else if (i == 2) printf("%d ", f2);
                else { f3 = f1 + f2; printf("%d ", f3); f1 = f2; f2 = f3; }
            }
            printf("\n");
            break;
        }

        case 5:
            printf("La revedere!\n");
            break;

        default:
            printf("\n!!! OPTIUNE INEXISTENTA: Alegeti doar intre 1 si 5.\n");
        }
    } while (optiune != 5);

    return 0;
}