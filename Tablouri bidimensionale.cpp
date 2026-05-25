#include <iostream>

using namespace std;

int prim(int x) {
    if (x < 2) return 0;
    for (int i = 2; i * i <= x; i++) {
        if (x % i == 0) return 0;
    }
    return 1;
}

int main() {
    int n, a[100][100];
    int pare[10000], k_pare = 0;
    int prime[10000], k_prime = 0;
    int dp[100], k_dp = 0;
    int ds[100], k_ds = 0;
    int ts[10000], k_ts = 0;

    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] % 2 == 0) {
                pare[k_pare] = a[i][j];
                k_pare++;
            }
            if (prim(a[i][j])) {
                prime[k_prime] = a[i][j];
                k_prime++;
            }
            if (i == j) {
                dp[k_dp] = a[i][j];
                k_dp++;
            }
            if (i + j == n - 1) {
                ds[k_ds] = a[i][j];
                k_ds++;
            }
            if (i < j && i + j < n - 1) {
                ts[k_ts] = a[i][j];
                k_ts++;
            }
        }
    }

    for (int i = 0; i < k_pare; i++) cout << pare[i] << " ";
    cout << "\n";

    for (int i = 0; i < k_prime; i++) cout << prime[i] << " ";
    cout << "\n";

    for (int i = 0; i < k_dp; i++) cout << dp[i] << " ";
    cout << "\n";

    for (int i = 0; i < k_ds; i++) cout << ds[i] << " ";
    cout << "\n";

    for (int i = 0; i < k_ts; i++) cout << ts[i] << " ";
    cout << "\n";

    return 0;
}