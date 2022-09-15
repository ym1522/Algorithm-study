#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    int n;
    cin >> n;

    string output = "";
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            output += '*';
        }
        output += "\n";
    }
    cout << output << "\n";
    return 0;
}