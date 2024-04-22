#include<bits/stdc++.h>
using namespace std;

void maxHeapify(vector<int>&A, int k, int i){
    int start= i * k+1;
    int maxi = i * k + k+1;
    int largest = i;
    while(start < A.size() && start < maxi){
        if(A[start] > A[largest]){
            largest= start;
        }
        start++;

        
    }
    if( largest != i){
        // cout<<largest<<" "<<i;
        swap(A[largest], A[i]);
        maxHeapify(A, k, largest);
    }
}

void solve(vector<int>& A, int k)
{
    // cout<<"HI";
    // return;
    for(int i = (A.size()/k )+ 1; i >=0; i--){
        // cout<<i<<": i"<<endl;
        maxHeapify(A, k, i);
    }




}
