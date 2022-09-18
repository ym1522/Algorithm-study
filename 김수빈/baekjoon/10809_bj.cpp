#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    string str;
    string output = "";
    getline(cin, str);
    int idx;
    for (int i = 0; i < 26; i++) {
        idx = -1;
        for (int j = 0; j < str.length(); j++) {
            if ((int)str[j] == i + 97) {
                idx = j;
                break;
            }
        }
        output += to_string(idx) + " ";
    }
    cout << output << "\n";
    return 0;
}