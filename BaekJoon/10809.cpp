#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solution(vector<int> v ,string a) {
    for (int j = 97; j <= 127; j++)
    {
        for (int i = 0; i < a.size(); i++)
        {
            if(a[i] == j && v[j-97] == -1) {
                v[j-97] = i;
            }
        }
    }
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
}

int main() {
    string a;
    cin >> a;
    vector<int> v (26,-1);
    solution(v,a);
    return 0;
}