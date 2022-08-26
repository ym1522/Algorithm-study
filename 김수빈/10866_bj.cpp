#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <math.h>

using namespace std;

class Deque {

public:
    int nums[20001] = {};
    int len = 0;
    int head = 10000;
    int top = 10000;
    int empty() {
        return (int)(len == 0);
    }
    int size() {
        return len;
    }
    int front() {
        if (len == 0) return -1;
        return nums[head];
    }
    int back() {
        if (len == 0) return -1;
        return nums[top];
    }
    void push_front(int x) {
        if (len == 0) nums[head] = x;
        else {
            head -= 1;
            nums[head] = x;
        }
        len += 1;
    }
    void push_back(int x) {
        if (len == 0) nums[top] = x;
        else {
            top += 1;
            nums[top] = x;
        }
        len += 1;
    }
    int pop_back() {
        if (len == 0) return -1;
        int t = nums[top];
        if (head < top) top -= 1;
        len -= 1;
        return t;
    };
    int pop_front() {
        if (len == 0) return -1;
        int t = nums[head];
        if (head < top) head += 1;
        len -= 1;
        return t;
    };
};
int main()
{
    int n;
    scanf_s("%d", &n);
    cin.ignore();

    Deque deque;
    string str;
    for (int i = 0; i < n; i++) {
        getline(cin, str);
        if (str.substr(0, 9) == "push_back") deque.push_back(stoi(str.substr(10)));
        if (str.substr(0, 10) == "push_front") deque.push_front(stoi(str.substr(11)));
        else if (str == "front") printf("%d\n", deque.front());
        else if (str == "back") printf("%d\n", deque.back());
        else if (str == "pop_front") printf("%d\n", deque.pop_front());
        else if (str == "pop_back") printf("%d\n", deque.pop_back());
        else if (str == "size") printf("%d\n", deque.size());
        else if (str == "empty") printf("%d\n", deque.empty());
    }
    return 0;
}