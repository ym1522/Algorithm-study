#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int solution(vector<int> &nums, int n, int m) {
    int val = nums.at(m);
    int cnt = 1;
    int top;
    
    int max_val = *max_element(nums.begin(), nums.end());
    while (m > 0 || max_val > val) {
        top = nums.at(0);
        nums.erase(nums.begin());
        
        max_val = *max_element(nums.begin(), nums.end());

        if (top >= max_val) cnt += 1;
        else nums.push_back(top);

        m -= 1;
        if (m < 0) m += nums.size();
    }
    return cnt;
}

int main()
{
    int k, n, m;
    cin >> k;
    cin.ignore();

    vector<int> nums;
    int tmp;
    for (int i = 0; i < k; i++) {
        scanf_s("%d %d", &n, &m);

        for (int j = 0; j < n; j++) {
            scanf_s(" %d", &tmp);
            nums.push_back(tmp);
        }
        
        cout << solution(nums, n, m) << "\n";
        nums.clear();
    }
    return 0;
}