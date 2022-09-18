#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;

    int R;
    string S, output;
    
    for (int i = 0; i < T; i++) {
        cin >> R >> S;
        output = "";
        for (int j = 0; j < S.length(); j++) {
            for (int k = 0; k < R; k++) {
                output += S[j];
            }
        }
        cout << output << "\n";
        
    }

    return 0;
}