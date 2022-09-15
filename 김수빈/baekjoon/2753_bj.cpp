#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    int year;
    cin >> year;

    int is_leap = 0;
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        is_leap = 1;
    }
    cout << is_leap << "\n";
    return 0;
}