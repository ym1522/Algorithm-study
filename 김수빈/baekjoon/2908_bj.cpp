#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    string a, b;
    cin >> a >> b;

    std::reverse(a.begin(), a.end());
    std::reverse(b.begin(), b.end());

    if (a > b) {
        cout << a << "\n";
    }
    else {
        cout << b << "\n";
    }

    return 0;
}