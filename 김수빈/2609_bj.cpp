#include <iostream>
#include <stdio.h>
#include <string>
#include <stdlib.h>
using namespace std;

int gcd(int a, int b) {
    int c = a % b;
    while (c > 0) {
        a = max(b, c);
        b = min(b, c);
        c = a % b;
    }
    return b;
}
int lcm(int a, int b) {
    int answer = 0;
    for (int i = max(a, b); i <= a * b; i++) {
        if (i % a == 0 && i % b == 0) {
            answer = i;
            break;
        }
    }
    return answer;
}
int main()
{
    int x, y;
    cin >> x >> y;

    int a, b;
    if (x > y) {
        a = x; b = y;
    }
    else {
        a = y; b = x;
    }
    cout << gcd(a, b) << "\n";
    cout << lcm(a, b) << "\n";

    return 0;
}