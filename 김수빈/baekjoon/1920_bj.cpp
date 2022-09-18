#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

bool compare(int a, int b) {
    return a < b;
}

int find_binary(int* &nums, int i, int j, int key) {
    if (i == j) {
        if (nums[i] == key) return i;
        else return -1;
    }
    int mid = (i + j) / 2;
    if (nums[mid] == key) return mid;
    else if (nums[mid] > key) return find_binary(nums, i, mid, key);
    else return find_binary(nums, mid + 1, j, key);

}
int main()
{
    int n, m, k;
    int* nums;
    int* tgts;
    
    scanf("%d", &n);
    cin.ignore();

    nums = new int[n];
    for (int i = 0; i < n; i++) scanf(" %d", &nums[i]);
    sort(nums, nums + n, compare);
    
    scanf("%d", &m);
    cin.ignore();

    tgts = new int[m]();
    for (int i = 0; i < m; i++) scanf(" %d", &tgts[i]);
  
    for (int i = 0; i < m; i++) {
        k = find_binary(nums, 0, n - 1, tgts[i]);
        if (k >= 0) printf("1\n");        
        else  printf("0\n");
    }    

    delete[] nums, tgts;
    return 0;
}