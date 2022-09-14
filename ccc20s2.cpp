#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>
#include <stdio.h>
#include <string.h>
#include <math.h>
using namespace std;

int N, M;
const int MAX = 1001;

int adj[MAX][MAX];
bool visited[1000001];
queue<int> q;


void bfs(){
    //int dest = adj[N][M];
    int dest = N*M;
    memset(visited,0,1000001*sizeof(bool));
    q.push(adj[1][1]);
    visited[adj[1][1]]=true;
    while(q.size()>0){
        int n = q.front();
        if(n==dest){
            cout<<"yes"<<endl;
            return;
        }
        q.pop();
        //factors(n);
        int root = sqrt(n);
        for(int i=1;i<=root;i++){
            if(n%i==0){
                if(i<=N && n/i<=M && !visited[adj[i][n/i]]){
                    q.push(adj[i][n/i]);
                    //cout<<i<<"  "<<n/i<<endl;
                    visited[adj[i][n/i]]=true;
                }
                if(i<=M && n/i<=N && !visited[adj[n/i][i]]){
                    q.push(adj[n/i][i]);
                    //cout<<n/i<<"  "<<i<<endl;
                    visited[adj[n/i][i]]=true;
                }
            }
        }

    }

    cout<<"no"<<endl;

}

int main(){
    cin>>N;cin>>M;
    memset(adj,0,MAX*MAX*sizeof(int));
    for(int i=1;i<=N;i++){
        for(int j=1;j<=M;j++){
            int temp; cin>>temp;
            adj[i][j]=temp;
        }
    }
    bfs();

    return 0;
}
