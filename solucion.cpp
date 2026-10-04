#include <bits/stdc++.h>
using namespace std;

const int VMAX = 58;          // cota superior para los b_i (ver Lema 1)
const int NP   = 16;          // primos <= 53
int primos[NP] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53};
int n, a[105], msk[VMAX + 1]; // msk[v] = conjunto de primos que dividen a v
int memo[105][1 << NP];       // memo[i][S] = K(i, S), -1 = no calculado
long long visitados = 0;

// K(i, S): costo minimo de elegir b_i..b_n si los primos de S ya estan usados
int K(int i, int S) {
    if (i == n + 1) return 0;                       // caso base
    int &r = memo[i][S];
    if (r != -1) return r;                          // memoizacion
    visitados++;
    r = INT_MAX;
    for (int v = 1; v <= VMAX; v++)                 // decision: valor de b_i
        if ((msk[v] & S) == 0)                      // alternativa factible
            r = min(r, abs(a[i] - v) + K(i + 1, S | msk[v]));
    return r;
}

int main() {
    for (int v = 1; v <= VMAX; v++)
        for (int j = 0; j < NP; j++)
            if (v % primos[j] == 0) msk[v] |= 1 << j;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
    memset(memo, -1, sizeof(memo));
    auto t0 = chrono::steady_clock::now();
    int opt = K(1, 0);
    double ms = chrono::duration<double, milli>(chrono::steady_clock::now() - t0).count();
    // reconstruccion de un b optimo
    int S = 0;
    for (int i = 1; i <= n; i++)
        for (int v = 1; v <= VMAX; v++)
            if ((msk[v] & S) == 0 && abs(a[i] - v) + K(i + 1, S | msk[v]) == K(i, S)) {
                printf("%d ", v); S |= msk[v]; break;
            }
    printf("\n");
    fprintf(stderr, "costo=%d estados=%lld ms=%.2f\n", opt, visitados, ms);
}
