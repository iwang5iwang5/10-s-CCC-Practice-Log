#include<iostream>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

long long N;
long long P[200001];
long long W[200001];
long long D[200001];

long long absV(long long i){
    if(i<0){
        return i*(-1);
    }
    return i;
}
long long calc(long long pos){
    long long tot = 0;
    for(long long i=1;i<=N;i++){
        if(P[i]==pos || (P[i]<pos && P[i]+D[i]>=pos) || (P[i]>pos && P[i]-D[i]<=pos)){
            continue;
        } else {
            if(P[i]<pos){
                tot+=absV(P[i]+D[i]-pos)*W[i];
            } else {
                tot+=absV(P[i]-D[i]-pos)*W[i];
            }
        }
    }
    return tot;
}
long long binary(long long left, long long right){
    while(left<right){
        long long mid = (left+right)/2;
        if(mid==left || mid==right){
            return calc(mid);
        }
        //cout<<calc(mid-1)<<"  "<<calc(mid)<<"  "<<calc(mid+1)<<endl;
        if(calc(mid-1)>=calc(mid) && calc(mid)>=calc(mid+1)){
            left=mid;
        } else if(calc(mid-1)<=calc(mid) && calc(mid)<=calc(mid+1)){
            right = mid;
        } else{
            return calc(mid);
        }
    }
    //cout<<"failed"<<endl;
    return calc(right);
}

int main(){
    cin>>N;
    long long minP = 10000000001;
    long long maxP = -1;
    for(long long i=1;i<=N;i++){
        long long tempP,tempW,tempD;
        cin>>tempP; cin>>tempW; cin>>tempD;
        P[i]=tempP; W[i]=tempW; D[i]=tempD;
        if(tempP<minP){
            minP=tempP;
        }
        if(tempP>maxP){
            maxP=tempP;
        }
    }
    cout<<binary(minP,maxP);
}
