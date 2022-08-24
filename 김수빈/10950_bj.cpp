#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    int a, b;
    for (int i = 0; i < t; i++) {
        scanf_s("%d %d", &a, &b);
        cout << a + b << "\n";
    }
    return 0;
}