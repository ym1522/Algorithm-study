#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    int h, m;
    cin >> h >> m;

    if (m < 45) {
        h -= 1;
        m = 60 + m - 45;
        if (h < 0) h += 24;

    }
    else {
        m -= 45;
    }
    printf("%d %d", h, m);
    return 0;
}