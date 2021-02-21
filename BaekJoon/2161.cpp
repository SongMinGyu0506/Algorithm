#include <iostream>
#include <vector>
using namespace std;


void solution(vector<int> v) {
    int size;
    size = v.size();
    for (int i = 0; i < size; i++)
    {
        int temp = v.front();
        cout << temp << " ";
        v.erase(v.begin());
        temp = v.front();
        v.push_back(temp);
        v.erase(v.begin());
    }
}

int main() {
    int N;
    cin >> N;
    vector<int> v;
    for (int i = 1; i <= N; i++)
    {
        v.push_back(i);
    }
    solution(v);
    return 0;
}