#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int min = 1000001;
    int max = -1000001;
    
    int tmp;
    for (int i = 0; i < n; i++) {
        scanf(" %d", &tmp);

        if (tmp < min) {
            min = tmp;
        }
        if (tmp > max) {
            max = tmp;
        }
    }
    cout << min << ' ' << max << endl;
    return 0;
}   
