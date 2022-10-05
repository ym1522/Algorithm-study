#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <math.h>
#include <stdlib.h>
using namespace std;

#define MAX_DIGITS 7

int solution(int n) {
    int k, digits;
    char num_char[MAX_DIGITS + sizeof(char)];

    int answer = 0;
    for (int i = 1; i < n; i++) {
        sprintf(num_char, "%d", i);
        k = i;
        digits = log10(i) + 1;
        for (int j = 0; j < digits; j++) {
            k += num_char[j] - '0';
        }
        if (k == n) {
            answer = i;
            break;
        }
    }
    return answer;
}

int main()
{
    int n;
    cin >> n;
    cin.ignore();

    cout << solution(n) << "\n";
    
    return 0;
}