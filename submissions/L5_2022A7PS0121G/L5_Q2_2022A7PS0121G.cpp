#include<bits/stdc++.h>
using namespace std;

void maxHeapify(vector<int> &arr, int k, int n, int a){
    int largest = a;
    vector<int> nodes(k);
    for(int i=0; i<k; i++){
        nodes[i] = a*k + i + 1;
    }

    for(int i=0; i<k; i++){
        if(nodes[i] < n && arr[largest] < arr[nodes[i]]){
            largest = nodes[i];
        }
    }

    if(largest != a){
        int temp = arr[a];
        arr[a] = arr[largest];
        arr[largest] = temp;
        maxHeapify(arr, k, n, largest);
    }
}


void buildHeap(vector<int> &arr, int k, int n){
    int start = (double)n/(double)k;
    for(int i=start; i>=0; i--){
        maxHeapify(arr, k, n, i);
    }
}

void solve(vector<int>& A, int k)
{
    int n = A.size();
    buildHeap(A, k, n);
}
