#include<bits/stdc++.h>
using namespace std;

int find_index(vector<int>& nums, int start, int end, int val){
    if(start > end){
        return -1;
    }
    int mid = start + (end - start)/2;
    if(nums[mid] == val){
        return mid;
    } else if (nums[mid] > val){
        return find_index(nums, start, mid -1, val);
    } else{
        return find_index(nums, mid+1, end, val);
    }
}

int solve(vector<int>& nums)
{
    int i = 0;
    int j = nums.size()-1;
    sort(nums.begin(), nums.end());
    int sum;
    int total =0;
    // for(int i =0; i < nums.size(); i++){
    //     cout<<nums[i]<<" ";
    // }
    // cout<<endl;
    for(int i =0; i < nums.size(); i++){
        if(i > 0 && nums[i-1] == nums[i]){
            continue;
        }
        for(int j = nums.size() -1; j >i; j--){
            if(j < nums.size()-1 && nums[j] == nums[j+1]){
                continue;
            }
        sum = -(nums[i] + nums[j] );
        int p = find_index(nums, i+1, j-1, sum);
        if(p != -1){
            total++;
            // cout<<i<<" "<<j<<" "<<p<<endl;
        }}

    }


    return total;
}
