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
    vector<pair<int, int>> people;
    vector<string> names;

    cin.ignore();
    int age;
    char name[101];
    string str_name;
    
    for (int i = 0; i < n; i++) {
        scanf_s("%d %s", &age, name, 101);        
        people.push_back({ age, i });
        
        str_name = name;
        names.push_back(str_name);
        
    }
    sort(people.begin(), people.end(), compare);

    for (int i = 0; i < n; i++) {
        printf("%d %s\n", people[i].first, names[people[i].second].c_str());
    }

    return 0;
} 