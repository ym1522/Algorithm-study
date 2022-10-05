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
    cin >> n;
    cin.ignore();

    int w, h;
    vector<pair<int, int>> people;
    for (int i = 0; i < n; i++) {
        scanf_s("%d %d", &w, &h);
        people.push_back({ w, h });
    }
    int rank;
    for (int i = 0; i < n; i++) {
        w = people[i].first;
        h = people[i].second;
        rank = 1;
        for (int j = 0; j < n; j++) {
            if (people[j].first > w && people[j].second > h) {
                rank += 1;
            }
        }
        cout << rank << " ";
    }

    return 0;
}