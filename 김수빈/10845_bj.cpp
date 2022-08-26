#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <math.h>

using namespace std;

class Queue {

public:
    vector<int> vec;
    int empty() {
        return (int)vec.empty();
    }
    int size() {
        return vec.size();
    }
    int front() {
        if (vec.empty()) return -1;
        return vec.front();
    }
    int back() {
        if (vec.empty()) return -1;
        return vec.back();
    }
    void push(int x) {
        vec.push_back(x);
    }
    int pop() {
        if (vec.empty()) return -1;
        int t = vec.front();
        vec.erase(vec.begin());
        return t;
    };
};
int main()
{
    int n;
    scanf_s("%d", &n);
    cin.ignore();
    
    Queue queue;
    string str;
    for (int i = 0; i < n; i++) {
        getline(cin, str);
        if (str.substr(0, 4) == "push") queue.push(stoi(str.substr(5)));
        else if (str == "front") printf("%d\n", queue.front());
        else if (str == "back") printf("%d\n", queue.back());
        else if (str == "pop") printf("%d\n", queue.pop());
        else if (str == "size") printf("%d\n", queue.size());
        else if (str == "empty") printf("%d\n", queue.empty());
    }
    return 0;
} 