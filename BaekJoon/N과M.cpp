#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

void solution(int counters, int N, int M, bool checker[],vector<int> v) {
    if(counters == M) {
        for (int i = 0; i < v.size(); i++)
        {
            cout << v[i] << " ";
        }
        cout << endl;
    }
    for (int i = 1; i <= N; i++)
    {
        if(!checker[i]) {
            checker[i] = true;
            v[counters] = i;
            solution(counters+1,N,M,checker,v);
            checker[i] = false;
        }
    }
}
int main() {
    int N, M;
    cin >> N >> M;
    bool checker[N+1] = {false};
    vector<int> v (M);
    int counter = 0;
    solution(counter,N,M,checker,v);
}