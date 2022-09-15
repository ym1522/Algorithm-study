#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <stdlib.h>
using namespace std;


bool compare(int a, int b) {
    return a < b;
}
int main()
{
    int n;
    cin >> n;

    int* nums = new int[n];
    for (int i = 0; i < n; i++) {
        scanf_s("%d", &nums[i]);
    }

    sort(nums, nums + n, compare);
    for (int i = 0; i < n; i++) {
        cout << nums[i] << "\n";
    }

    return 0;
}