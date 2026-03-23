#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;

    while (true) {
        cout << "\nIntroduceti un numar (sau un numar negativ pentru a iesi): ";
        cin >> n;

        // Conditia de exit din program
        if (n < 0) {
            cout << "Programul s-a incheiat.";
            break;
        }

        if (n == 0) {
            cout << "zero" << endl;
            continue; // Trecem la urmatoarea
        }

        if (n >= 1000) {
            cout << "Eroare: Te rog introdu un numar mai mic decat 1000." << endl;
            continue;
        }

        cout << "In litere: ";

        // 1. Sute
        int sute = n / 100;
        if (sute > 0) {
            if (sute == 1) cout << "o suta ";
            else if (sute == 2) cout << "doua sute ";
            else {
                string cifre[] = { "", "", "", "trei", "patru", "cinci", "sase", "sapte", "opt", "noua" };
                cout << cifre[sute] << " sute ";
            }
        }

        int rest = n % 100;
        int zeci = rest / 10;
        int unitati = rest % 10;

        // 2. Zeci si Unitati
        if (zeci == 0) {
            string u[] = { "", "unu", "doi", "trei", "patru", "cinci", "sase", "sapte", "opt", "noua" };
            if (unitati > 0) cout << u[unitati];
        }
        else if (zeci == 1) {
            string speciale[] = { "zece", "unsprezece", "doisprezece", "treisprezece", "paisprezece",
                                 "cincisprezece", "saisprezece", "sapteprezece", "optsprezece", "nouasprezece" };
            cout << speciale[unitati];
        }
        else {
            string z[] = { "", "", "douazeci", "treizeci", "patruzeci", "cincizeci",
                          "saizeci", "saptezeci", "optzeci", "nouazeci" };
            cout << z[zeci];

            if (unitati > 0) {
                cout << " si ";
                string u[] = { "", "unu", "doi", "trei", "patru", "cinci", "sase", "sapte", "opt", "noua" };
                cout << u[unitati];
            }
        }
        cout << endl; // Noua linie dupa fiecare numar afisat
    }

    return 0;
}