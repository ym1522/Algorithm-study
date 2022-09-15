#include <iostream>
#include <vector>
#include <stdlib.h>
#include <math.h>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	
	vector<int> vec;
	int a;
	for (int i = 0; i < n; i++){
		scanf("%d", &a);
		if (a != 0) vec.push_back(a);
		else vec.pop_back();
	}
	int sum = 0;
	for (int i = 0;i < vec.size(); i++){
		sum += vec.at(i);
	}
	if (sum >= pow(2, 31)) sum = pow(2, 31) - 1;
	cout << sum;
	
	return 0;
}