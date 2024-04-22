#include<bits/stdc++.h>
using namespace std;

int solve(vector<int>& nums)
{
    int n = nums.size();
    sort(nums.begin(), nums.end());
    int count = 0;
    for(int i = 0; i < n-2; i++){
        if(i != 0){
            while(i < n-2 && nums[i] == nums[i-1]){
                i++;
            }
        }
        int left = i+1;
        int right = n-1;

        int target = -nums[i];
        while(left < right){
            int sum = nums[left]+nums[right];

            if(left < right && target == sum){
                count++;
                left++;
                right--;
                while(left < right && nums[left] == nums[left-1]){
                    left++;
                }
                 while(left < right && nums[right] == nums[right+1]){
                    right--;
                }
            }
            else if(left < right && target < sum){
                right--;
                 while(left < right && nums[right] == nums[right+1]){
                    right--;
                }
            }
            else if(left < right && target > sum){
                left++;
                 while(left < right && nums[left] == nums[left-1]){
                    left++;
                }
            }
        }
    }


    return count;
}
