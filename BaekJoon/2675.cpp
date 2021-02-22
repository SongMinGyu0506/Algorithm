#include <iostream>
#include <string>
using namespace std;

void solution() {
    int A;
        string B;
        cin >> A >> B;
        for (int k = 0; k < B.size(); k++)
        {
            for (int j = 0; j < A; j++)
            {
                cout << B[k];
            }
        }
        cout << endl;
}

int main() {
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        solution();
    }
    return 0;
}