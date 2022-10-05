#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{

    int a, b, c;
    scanf_s("%d", &a);
    scanf_s("%d", &b);
    scanf_s("%d", &c);

    string p = to_string(a * b * c);
    int counts[10] = {};
    for (int i = 0; i < p.length(); i++) {
        counts[p[i] - '0'] += 1;
    }
    for (int i = 0; i < 10; i++) {
        cout << counts[i] << "\n";
    }
    return 0;
}