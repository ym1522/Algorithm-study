#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int n;
    scanf_s("%d", &n);
    
    int a[1000];
    int max = 0;
    for (int i = 0; i < n; i++) {
        scanf_s(" %d", &a[i]);
        if (max < a[i]) {
            max = a[i];
        }
    }
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += ((double)a[i] / (double)max * (double)100);
    }

    cout << sum/n << endl;
    return 0;
}   
