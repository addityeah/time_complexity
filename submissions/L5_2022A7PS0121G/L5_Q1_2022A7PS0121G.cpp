#include<bits/stdc++.h>
using namespace std;

int solve(vector<int>& nums)
{
    sort(nums.begin(), nums.end());
    int n = nums.size();
    int count = 0;
    unordered_set<int> s;
    for(int i=0; i<n; i++){
        int j = i+1;
        int k = n-1;
        if(s.find(nums[i]) != s.end()){
            continue;
        }
        while(j < k){
            if((nums[i] + nums[j] + nums[k]) == 0){
                count++;
                j++;
                k--;
            }
            else if((nums[i] + nums[j] + nums[k]) < 0){
                j++;
            }
            else{
                k--;
            }
        }
        s.insert(nums[i]);

    }
    return count;
}
