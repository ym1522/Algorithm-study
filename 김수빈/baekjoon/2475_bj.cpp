#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;

int main()
{
    int num, sum;
    sum = 0;
    for (int i = 0; i < 5; i++) {
        scanf_s(" %d", &num);
        sum += pow(num, 2);
    }
    cout << sum % 10 << "\n";
    return 0;
}