#include <stdio.h>

#define N 100

void sum_right_neighbour(int v[N], int n) {
    for (int i = 0; i < n - 1; i++) {
        v[i] += v[i + 1];
    }
}

void sum_left_neighbour(int v[N], int n) {
    for (int i = n - 1; i > 0; i--) {
        v[i] += v[i - 1];
    }
}

void product_exclude_self(int v[N], int n) {
    int v_prod[N];
    for (int i = 0; i < n; i++) {
        v_prod[i] = 1;
        for (int j = 0; j < n; j++) {
            if (i != j) {
                v_prod[i] *= v[j];
            }
        }
    }
    for (int i = 0; i < n; i++) {
        printf("%d ", v_prod[i]);
    }
    printf("\n");
}

void print_vector(int v[N], int n) {
    if (n <= 0) {
        printf("\n");
        return;
    }
    for (int i = 0; i < n; i++) {
        printf("%d ", v[i]);
    }
    printf("\n");
}

int main(void) {
    int v[N] = { 1, 2, 3, 4, 5 };
    int n = 5;
    char c;

    while (1) {
        if (scanf(" %c", &c) != 1) break;

        if (c == '0') {
            print_vector(v, n);
            break;
        }

        switch (c) {
        case '1':
            if (n > 0) {
                int min_idx = 0;
                for (int i = 1; i < n; i++) {
                    if (v[i] < v[min_idx]) min_idx = i;
                }
                for (int i = min_idx; i < n - 1; i++) {
                    v[i] = v[i + 1];
                }
                n--;
            }
            break;

        case '2':
            if (n > 0) {
                int max_idx = 0;
                for (int i = 1; i < n; i++) {
                    if (v[i] > v[max_idx]) max_idx = i;
                }
                for (int i = max_idx; i < n - 1; i++) {
                    v[i] = v[i + 1];
                }
                n--;
            }
            break;

        case '3':
            sum_right_neighbour(v, n);
            break;

        case '4':
            sum_left_neighbour(v, n);
            break;

        case '5':
            product_exclude_self(v, n);
            break;
        }
    }

    return 0;
}