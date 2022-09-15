#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
using namespace std;

bool compare(pair<int, int>& a, pair<int, int>& b) {
    if (a.first < b.first) return true;
    else if (a.first == b.first) return a.second < b.second;
    else return false;
}
int main()
{
    int n;
    scanf_s("%d", &n);
    string str;
    vector<pair<int, int>> coor;

    cin.ignore();
    int x, y;
    for (int i = 0; i < n; i++) {
        scanf_s("%d %d", &x, &y);
        coor.push_back({ x, y });
    }
    sort(coor.begin(), coor.end(), compare);

    for (int i = 0; i < n; i++) {
        printf("%d %d\n", coor[i].first, coor[i].second);
    }

    return 0;
}