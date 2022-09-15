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
        output += to_string(i) + "\n";
    }
    cout << output << "\n";
}