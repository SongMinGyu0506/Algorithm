#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N,K;
    cin >> N >> K;
    vector<int> v(N);
    for (int i = 0; i < v.size(); i++)
    {
        cin >> v[i];
    }
    int temp = NULL;
    for (int i = 0; i < v.size(); i++)
    {
        if(K%v[i] == 0) {
            if(temp == NULL) {
                temp = K/v[i];
            }
            else {
                if(temp > K/v[i])
                    temp = K/v[i];
            }
        }
    }
    cout << temp << endl;
    return 0;
}

