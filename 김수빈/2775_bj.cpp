#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;


int solution(int k, int n) {
    int** apart = new int* [k + 1];
    
    for (int i = 0; i < k + 1; i++) {
        apart[i] = new int[n]();
    }
    for (int i = 0; i < n; i++) {
        apart[0][i] = i + 1;
    }
    for (int i = 1; i < k + 1; i++) {
        for (int j = 0; j < n; j++) {
            if (j == 0) apart[i][j] = apart[i - 1][j];
            else apart[i][j] = apart[i - 1][j] + apart[i][j - 1];
        }
    }

    int sum = apart[k - 1][n - 1] + apart[k][n - 2];
    delete[] apart;
    return sum;
}

int main()
{
    int t, k, n;
    cin >> t;
    cin.ignore();

    for (int i = 0; i < t; i++) {
        scanf_s("%d", &k);
        scanf_s("%d", &n);

        cout << solution(k, n) << "\n";
    }
    return 0;
}