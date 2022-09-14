#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;
int main(){
    int M, N, K;
    cin>>M; cin>>N; cin>>K;
    int row[M+1];
    int col[N+1];
    memset(row,0,(M+1)*sizeof(int));
    memset(col,0,(N+1)*sizeof(int));
    for(int i=0;i<K;i++){
        string rc;
        int num;
        cin>>rc; cin>>num;
        if(rc=="R"){
            row[num]+=1;
            row[num]%=2;
        } else {
            col[num]+=1;
            col[num]%=2;
        }
    }
    int ans = 0;
    for(int i=1;i<=M;i++){
        for(int j=1;j<=N;j++){
            if((row[i]+col[j])%2!=0){
                ans+=1;
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}
