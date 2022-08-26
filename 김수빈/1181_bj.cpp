#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <stdlib.h>
using namespace std;


bool compare(string a, string b) {
    if (a.length() == b.length()) {
        return a < b;
    }
    return a.length() < b.length();
}
int main()
{
    int n;
    cin >> n;
    cin.ignore();

    string* words = new string[n];
    for (int i = 0; i < n; i++) {
        getline(cin, words[i]);
        
    }

    sort(words, words + n, compare);
    string prev = "";
    for (int i = 0; i < n; i++) {
        if (words[i].compare(prev) != 0) {
            cout << words[i] << "\n";
        }
        prev = words[i];
    }

    return 0;
}