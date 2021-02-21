#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

void BFS(int start, vector<vector<int>> jungjum, bool check_vertical[]) {
    queue<int> q;

    check_vertical[start] = true;
    int start_temp;
    q.push(start);

   do  {
       start_temp = q.front(); q.pop();
       
       for (int i = 0; i < jungjum[start_temp].size(); i++)
       {
           int D1 = jungjum[start_temp][i];
           if(check_vertical[D1] == false){
               q.push(D1);
               check_vertical[D1] = true;
           }
       }
       printf("%d ",start_temp);
   }
   while (!q.empty());
}

void DFS(int start, vector<vector<int>> jungjum, bool check_vertical[]) {
    check_vertical[start]=true;
    printf("%d ",start);

    for (int i = 0; i < jungjum[start].size(); i++)
    {
        int D1 = jungjum[start][i];
        if(check_vertical[D1] == false) {
            DFS(jungjum[start][i],jungjum,check_vertical);
        }
    }
}

int main() {
    int N,M,S;
    cin >> N >> M >> S;
    bool check_vertical[N+1] = {false};
    //vector<bool> check_vertical(N,false);
    vector<vector<int>> jungjum(N+1,vector<int>(0,0));

    for (int i = 0; i < M; i++)
    {
        int N1,N2;
        cin >> N1 >> N2;
        jungjum[N1].push_back(N2);
        jungjum[N2].push_back(N1);
    }

    for (int i = 0; i < jungjum.size(); i++)
    {
        sort(jungjum[i].begin(),jungjum[i].end());
    }
    

    DFS(S,jungjum,check_vertical);
    for (int i = 0; i < N+1; i++)
    {
        check_vertical[i] = false;
    }
    printf("\n");
    BFS(S,jungjum,check_vertical);
    return 0;
    
}