#include <iostream>
using namespace std;

typedef struct point{
	int x;
	int y;
}Point;


int main() {
	Point p1, p2, p3;
	cin >> p1.x >> p1.y >> p2.x >> p2.y >> p3.x >> p3.y;
	if((p2.y-p1.y) * (p3.x - p2.x) == (p3.y - p2.y) * (p2.x-p1.x)){
		cout << "0\n";
	}
	else if((p2.y-p1.y) * (p3.x - p2.x) < (p3.y - p2.y) * (p2.x-p1.x)){
		cout << "1\n";
	}
	else cout << "-1\n";
	return 0;
}