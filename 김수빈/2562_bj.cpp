#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int max = 0;
    int k = -1;
    int tmp;
    for (int i = 0; i < 9; i++) {
        scanf_s("%d", &tmp);
        if (tmp > max) {
            max = tmp;
            k = i + 1;
        }
    }
    cout << max << "\n" << k << "\n";
}