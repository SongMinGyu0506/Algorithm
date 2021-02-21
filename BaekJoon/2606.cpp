#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int counting_bfs(int start, vector<vector<int>> graph, bool check_vertex[]) {
    int counter = -1;
    queue<int> q;
    int temp_start = start;
    q.push(temp_start);

    while(!q.empty()) {
        temp_start = q.front(); q.pop();
        for (int i = 0; i < graph[temp_start].size(); i++)
        {
            int D1 = graph[temp_start][i];
            if(check_vertex[D1] == false) {
                q.push(D1);
                check_vertex[D1] = true;
                counter++;
            }
        }
    }
    return counter;
}

int main() {
    int V,E;

    cin >> V;
    cin >> E;

    vector<vector<int>> graph (V+1);
    bool check_vertex[V+1] = {false};

    for (int i = 0; i < E; i++)
    {
        int F1, F2;
        cin >> F1 >> F2;
        graph[F1].push_back(F2);
        graph[F2].push_back(F1);
    }

    for (int i = 0; i < graph.size(); i++)
    {
        stable_sort(graph[i].begin(),graph[i].end());
    }
    
    cout << counting_bfs(1,graph,check_vertex) << endl;
    return 0;
}