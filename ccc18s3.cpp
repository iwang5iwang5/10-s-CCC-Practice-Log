#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>
#include <stdio.h>
#include <string>
#include <string.h>
using namespace std;

class Node{
public:
    int r,c,steps;
    Node(){
        r=0;
        c=0;
        steps=0;
    }
    Node(int rN, int cN, int sN){
        r=rN;
        c=cN;
        steps=sN;
    }
};

int N, M;
const int MAX = 101;
const int MAXINT = 999999;
char grid[MAX][MAX]; //grid is the char based graph
int dist[MAX][MAX];
bool visited[MAX][MAX];
queue<Node> q;
vector<Node> cams;


void addnode(Node n, bool isConveyor){

    if(grid[n.r][n.c]=='W' || dist[n.r][n.c]==-1){
        return;
    }
    //cout<<n.r<<"   "<<n.c<<"   "<<grid[n.r][n.c]<<endl;
    if(isConveyor){
        if(!visited[n.r][n.c] || n.steps<dist[n.r][n.c]){
            //cout<<n.steps<<"   "<<dist[n.r][n.c]<<endl;
            //cout<<grid[n.r][n.c]<<visited[n.r][n.c]<<endl;
            q.push(n);
            visited[n.r][n.c]=true;
            dist[n.r][n.c]=n.steps;
            //cout<<n.steps<<"   "<<dist[n.r][n.c]<<endl;
        }
    } else {
        if(!visited[n.r][n.c] || n.steps<dist[n.r][n.c]){
            //cout<<n.steps<<"   "<<dist[n.r][n.c]<<endl;
            //cout<<grid[n.r][n.c]<<visited[n.r][n.c]<<endl;
            q.push(n);
            visited[n.r][n.c]=true;
            dist[n.r][n.c]=n.steps;
            //cout<<n.steps<<"   "<<dist[n.r][n.c]<<endl;
        }
    }

}


void getadj(Node n){
    int r, c, steps;
    r=n.r; c=n.c; steps=n.steps;
    if(dist[r][c]==-1 || grid[r][c]=='W'){
        return;
    }
    if(grid[r][c]=='.' || grid[r][c]=='S'){
        addnode(Node(r-1,c,steps+1),false);
        addnode(Node(r+1,c,steps+1),false);
        addnode(Node(r,c-1,steps+1),false);
        addnode(Node(r,c+1,steps+1),false);
    }
    if(grid[r][c]=='L'){
        addnode(Node(r,c-1,steps),true);
    }
    if(grid[r][c]=='R'){
        addnode(Node(r,c+1,steps),true);
    }
    if(grid[r][c]=='U'){
        addnode(Node(r-1,c,steps),true);
    }
    if(grid[r][c]=='D'){
        addnode(Node(r+1,c,steps),true);
    }
}



void handlecamera(){
    for(int i=0;i<cams.size();i++){
        int x,y;
        x = cams[i].r;
        y = cams[i].c;
        while(true){
            if(grid[x][y]=='W'){
                break;
            }
            if(grid[x][y]=='.' || grid[x][y]=='S'){
                dist[x][y]=-1;
            }
            x--;
        }
        x = cams[i].r;
        y = cams[i].c;
        while(true){
            if(grid[x][y]=='W'){
                break;
            }
            if(grid[x][y]=='.' || grid[x][y]=='S'){
                dist[x][y]=-1;
            }
            x++;
        }
        x = cams[i].r;
        y = cams[i].c;
        while(true){
            if(grid[x][y]=='W'){
                break;
            }
            if(grid[x][y]=='.' || grid[x][y]=='S'){
                dist[x][y]=-1;
            }
            y--;
        }
        x = cams[i].r;
        y = cams[i].c;
        while(true){
            if(grid[x][y]=='W'){
                break;
            }
            if(grid[x][y]=='.' || grid[x][y]=='S'){
                dist[x][y]=-1;
            }
            y++;
        }
    }
}
void findpath(int sx, int sy){

    memset(visited,0,MAX*MAX*sizeof(bool));
    memset(dist,MAXINT,MAX*MAX*sizeof(bool));
    handlecamera();
    if(dist[sx][sy]==-1){
        //cout<<"cant start"<<endl;
        return;
    }
    q.push(Node(sx,sy,0));
    visited[sx][sy]=true;
    dist[sx][sy]=0;
    while(q.size()>0){
        Node cur = q.front();
        q.pop();
        getadj(cur);
    }
}

int main(){
    int sx, sy;
    cin>>N;cin>>M;
    for(int i=0;i<N;i++){
        string temp;
        cin>>temp;
        for(int j=0;j<temp.length();j++){
            grid[i][j]=temp.at(j);
            if(temp.at(j)=='C'){
                cams.push_back(Node(i,j,0));
            }
            if(temp.at(j)=='S'){
                sx=i;
                sy=j;
            }
        }
    }
    findpath(sx, sy);
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if(grid[i][j]=='.'){
                if(!visited[i][j]){
                    cout<<-1<<endl;
                } else {
                    cout<<dist[i][j]<<endl;
                }
            }
        }
    }

    return 0;
}
