#include<bits/stdc++.h>
using namespace std;

void max_heapify(vector<int>& A, int k, int i)
{   
    int n = A.size();
    int largest = i;
    for(int j = 1; j <= k; j++)
    {
        if((k*i + j) < n && A[k*i + j] > A[largest]){
            largest = k*i + j;
        }
    }
    if(largest != i)
    {
        swap(A[largest], A[i]);
        max_heapify(A, k, largest);
    }
        
    return;

}

void build_max_heap(vector<int>& A, int k)
{
    int n = A.size();
    for(int i = (n-2)/k; i >= 0; i--)
    {
        max_heapify(A, k, i);
    }
    return;
}

void solve(vector<int>& A, int k)
{
    build_max_heap(A, k);
    return;
}
