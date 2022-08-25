#include <iostream>
#include <stdio.h>
#include <string>
#include <stdlib.h>
using namespace std;

int main()
{
    int* num = new int[8];
    for (int i = 0; i < 8; i++) {
        scanf_s(" %d", &num[i]);
    }
    int sum = 0;
    for (int i = 1; i < 8; i++) {
        if (num[i - 1] > num[i]) {
            sum += -1;
        }
        else {
            sum += 1;
        }
    }
    if (sum == 7) {
        cout << "ascending";
    }
    else if (sum == -7) {
        cout << "descending";
    }
    else {
        cout << "mixed";
    }
    delete[] num;
    return 0;
}