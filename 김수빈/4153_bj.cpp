#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

int main() {
	int a, b, c;
	cin >> a >> b >> c;
	int sq_a, sq_b, sq_c;
	while (a != 0 && b != 0 && c != 0){
		sq_a = pow(a, 2);
		sq_b = pow(b, 2);
		sq_c = pow(c, 2);
		
		if ((sq_a + sq_b == sq_c)|| (sq_a + sq_c == sq_b) || (sq_c + sq_b == sq_a)){
			cout << "right" << "\n";
		}
		else{
			cout << "wrong" << "\n";
		}
		cin >> a >> b >> c;
	}
	return 0;
}