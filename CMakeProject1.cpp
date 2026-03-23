#include <stdio.h>

int main() {
    int n;

    while (1) { // In C, folosim 1 pentru true
        printf("\nIntroduceti un numar (sau un numar negativ pentru a iesi): ");

        // Citim numarul. Folosim %d pentru intregi.
        if (scanf("%d", &n) != 1) {
            // Curatam buffer-ul in caz de input gresit (litere)
            while (getchar() != '\n');
            continue;
        }

        // Conditia de exit din program
        if (n < 0) {
            printf("Programul s-a incheiat.\n");
            break;
        }

        if (n == 0) {
            printf("zero\n");
            continue;
        }

        if (n >= 1000) {
            printf("Eroare: Te rog introdu un numar mai mic decat 1000.\n");
            continue;
        }

        printf("In litere: ");

        // 1. Sute
        int sute = n / 100;
        if (sute > 0) {
            if (sute == 1) {
                printf("o suta ");
            }
            else if (sute == 2) {
                printf("doua sute ");
            }
            else {
                // In C folosim char* pentru siruri de caractere
                char* cifre[] = { "", "", "", "trei", "patru", "cinci", "sase", "sapte", "opt", "noua" };
                printf("%s sute ", cifre[sute]);
            }
        }

        int rest = n % 100;
        int zeci = rest / 10;
        int unitati = rest % 10;

        // 2. Zeci si Unitati
        if (zeci == 0) {
            char* u[] = { "", "unu", "doi", "trei", "patru", "cinci", "sase", "sapte", "opt", "noua" };
            if (unitati > 0) printf("%s", u[unitati]);
        }
        else if (zeci == 1) {
            char* speciale[] = { "zece", "unsprezece", "doisprezece", "treisprezece", "paisprezece",
                                 "cincisprezece", "saisprezece", "sapteprezece", "optsprezece", "nouasprezece" };
            printf("%s", speciale[unitati]);
        }
        else {
            char* z[] = { "", "", "douazeci", "treizeci", "patruzeci", "cincizeci",
                          "saizeci", "saptezeci", "optzeci", "nouazeci" };
            printf("%s", z[zeci]);

            if (unitati > 0) {
                printf(" si ");
                char* u[] = { "", "unu", "doi", "trei", "patru", "cinci", "sase", "sapte", "opt", "noua" };
                printf("%s", u[unitati]);
            }
        }
        printf("\n"); // Noua linie dupa fiecare numar afisat
    }

    return 0;
}