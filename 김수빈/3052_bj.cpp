#include <iostream>
#include <stdio.h>
#include <string>
#include <set>
using namespace std;

int main()
{
    int a;
    set<int> s;
    while (cin >> a) {
        s.insert(a % 42);
    }
    cout << s.size() << "\n";
    return 0;
}