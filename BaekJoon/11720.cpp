#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    char A[N];
    cin >> A;
    int result = 0;
    for (int i = 0; i < N; i++)
    {
        int temp = A[i] - '0';
        result = result + temp;
    }
    cout << result << endl;
    return 0;
}