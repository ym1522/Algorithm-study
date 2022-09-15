#include <iostream>
#include <stdio.h>
#include <string>
#include <stdlib.h>
using namespace std;

int main()
{
    int n;
    scanf_s("%d", &n);

    int k = 1;
    int i = 0;
    while(n > k) {
        k = i * 6 + k;
        i += 1;
    }
    if (n == 1) {
        cout << 1;
    }
    else {
        cout << i;
    }

    return 0;
}