#include <iostream>
#include <vector>
using namespace std;

void solution(int A, int B, int C) {
    if(B >= C) {
        cout << "-1" << endl;
    }
    else {
        int result = A/(C-B)+1;
        cout << result << endl;
    }
}

int main() {
    int A,B,C;
    cin >> A >> B >> C;
    solution(A,B,C);
    return 0;
}