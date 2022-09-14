#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
using namespace std;

int main()
{
    int n;
    scanf_s(" %d", &n);
    string str;
    vector<int> vec;

    cin.ignore();
    for (int i = 0; i < n; i++) {
        getline(cin, str);
        if (str.substr(0, 4) == "push") {
            vec.push_back(stoi(str.substr(5)));
        }
        else if (str == "top") {
            if (vec.empty()) printf("-1\n");
            else printf("%d\n", vec.back());
        }
        else if (str == "size") printf("%d\n", vec.size());
        else if (str == "empty") printf("%d\n", (int)vec.empty());
        else if (str == "pop") {
            if (vec.empty()) printf("-1\n");
            else {
                printf("%d\n", vec.back());
                vec.pop_back();
            }
        }
    }

    return 0;
}