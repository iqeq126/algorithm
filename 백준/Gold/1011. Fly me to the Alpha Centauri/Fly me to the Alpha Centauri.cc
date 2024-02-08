#include <iostream>
using namespace std;
void Warp(long long x, long long y) {
	long long t = y - x, k = 1, ans, i = 0;
	if (t < 4) ans = t;
	else {
		while (1) {
			t -= 2 * k;
			k++;
			if (t == 0) {
				ans = k * 2 - 2;
				break;
			}
			else if (t > 0 && t <= k) {
				ans = 2 * k - 1;
				break;
			}
			else if (t > k && t < 2*k) {
				ans = 2 * k;
				break;
			}
		}
	}
	cout << ans << "\n";
}


int main() {
	long long  test, x, y;
	cin >> test;
	while (test--) {
		cin >> x >> y;
		Warp(x, y);
	}
	return 0;
}