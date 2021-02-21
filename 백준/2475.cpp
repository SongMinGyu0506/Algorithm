#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int A,B,C,D,E;
    cin >> A >> B >> C >> D >> E;
    int temp = pow(A,2)+pow(B,2)+pow(C,2)+pow(D,2)+pow(E,2);
    int temp2 = temp%10;
    cout << temp2 << endl;
    return 0;
}