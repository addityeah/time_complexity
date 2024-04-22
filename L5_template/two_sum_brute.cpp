#include <bits/stdc++.h>
using namespace std;

int solve(vector<int>& nums, int target) {
    int n = nums.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] == target) {
                return 0;
            }
        }
    }
    return 0; // No solution found
}