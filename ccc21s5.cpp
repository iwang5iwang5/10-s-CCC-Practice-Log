#include<iostream>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

int N, M;
int sequence[150001];
vector<int> factors[150001];

void handle(int p1, int p2, int val){
    for(int i=p1;i<=p2;i++){
        factors[i].push_back(val);
    }
}

int LcmOfArray(vector<int> arr, int start){
    if(arr.size()==0){
        return 1;
    }
    if (start == arr.size()-1){
        return arr[start];
    }
    int a = arr[start];
    int b = LcmOfArray(arr, start+1);
    return (a*b/__gcd(a,b));
}

int GcdOfArray(vector<int>& arr, int idx)
{
    if (idx == arr.size() - 1) {
        return arr[idx];
    }
    int a = arr[idx];
    int b = GcdOfArray(arr, idx + 1);
    return __gcd(a, b);
}

int main(){
    memset(sequence,1,150001*sizeof(int));
    cin>>N; cin>>M;

    int req[M][3];
    for(int i=0;i<M;i++){
        int pos1, pos2, gcd;
        cin>>pos1; cin>>pos2; cin>>gcd;
        req[i][0]=pos1;
        req[i][1]=pos2;
        req[i][2]=gcd;
        handle(pos1,pos2,gcd);
    }

    for(int i=0;i<=N;i++){
        sequence[i]=LcmOfArray(factors[i],0);
    }

    for(int i=0;i<M;i++){
        vector<int> elements;
        for(int j=req[i][0];j<=req[i][1];j++){
            elements.push_back(sequence[j]);
        }
        //cout<<"done1"<<endl;
        if(GcdOfArray(elements,0)!=req[i][2]){
            cout<<"Impossible"<<endl;
            return 0;
        }
        //cout<<"done2"<<endl;
    }

    for(int i=1;i<=N;i++){
        cout<<sequence[i]<<" ";
    }
    return 0;
}


