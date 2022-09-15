#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore();

    string str;
    int* score;
    int total;
    for (int i = 0; i < n; i++) {
        getline(cin, str);
        score = new int[str.length()]();
        total = 0;
        for (int j = 0; j < str.length(); j++) {
            if ((int)str[j] == 79) {
                if (j == 0) {
                    score[j] = 1;
                }
                else {
                    score[j] = score[j - 1] + 1;
                }
                total += score[j];
            }
        }
        delete[] score;
        cout << total << "\n";
    }
    return 0;
}