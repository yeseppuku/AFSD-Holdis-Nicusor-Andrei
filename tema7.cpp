#include <iostream>

using namespace std;

int bisect(int an) {
    if (an % 400 == 0) return 1;
    if (an % 100 == 0) return 0;
    if (an % 4 == 0) return 1;
    return 0;
}

int zile_luna(int l, int a) {
    int z[13] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
    if (l == 2 && bisect(a)) return 29;
    return z[l];
}

int valid(int z, int l, int a) {
    if (a < 1) return 0;
    if (l < 1 || l > 12) return 0;
    if (z < 1 || z > zile_luna(l, a)) return 0;
    return 1;
}

void urmatoarea(int& z, int& l, int& a) {
    z++;
    if (z > zile_luna(l, a)) {
        z = 1;
        l++;
        if (l > 12) {
            l = 1;
            a++;
        }
    }
}

long long calcul_zile(int z, int l, int a) {
    long long total = 0;
    for (int i = 1; i < a; i++) {
        if (bisect(i)) total += 366;
        else total += 365;
    }
    for (int i = 1; i < l; i++) {
        total += zile_luna(i, a);
    }
    total += z;
    return total;
}

int main() {
    int z1, l1, a1;
    int z2, l2, a2;

    cin >> z1 >> l1 >> a1;
    cin >> z2 >> l2 >> a2;

    if (!valid(z1, l1, a1) || !valid(z2, l2, a2)) {
        cout << "Date invalide\n";
        return 0;
    }

    long long diferenta = calcul_zile(z1, l1, a1) - calcul_zile(z2, l2, a2);
    if (diferenta < 0) {
        diferenta = -diferenta;
    }

    int uz1 = z1, ul1 = l1, ua1 = a1;
    urmatoarea(uz1, ul1, ua1);

    int uz2 = z2, ul2 = l2, ua2 = a2;
    urmatoarea(uz2, ul2, ua2);

    cout << uz1 << " " << ul1 << " " << ua1 << "\n";
    cout << uz2 << " " << ul2 << " " << ua2 << "\n";
    cout << diferenta << "\n";

    return 0;
}