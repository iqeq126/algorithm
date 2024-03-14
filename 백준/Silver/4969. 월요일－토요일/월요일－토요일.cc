#include <iostream>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n = 0, i = 0, buf = 0;
    int tmp = 6, idx = 0;
    int M_S[40000] = { 0 };
    while (tmp <= 300010) {
        for (i = 0; i < idx; i++) {
            if (tmp % M_S[i] == 0) {
                buf++;
                break;
            }
        }
        if (buf == 0) {
            M_S[idx] = tmp;
            idx++;
        }
        buf = 0;
        if (tmp % 7 == 1) tmp += 5;
        else if (tmp % 7 == 6) tmp += 2;
    }
    while (1) {
        cin >> n;
        i = 0;
        if (n == 1) {
            return 0;
        }
        cout << n << ":";
        while (M_S[i] <= n) {
            if (n % M_S[i] == 0) cout << " " << M_S[i];
            i++;
        }
        cout << endl;
    }
    return 0;
}