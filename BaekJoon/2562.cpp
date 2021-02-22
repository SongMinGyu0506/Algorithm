#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v (10);
    int temp = 0;
    int temp2 = 0;
    for (int i = 1; i < 10; i++)
    {
        cin >> v[i];
    }
    for (int i = 1; i < 10; i++)
    {
        if(temp < v[i]) {
            temp2 = i;
            temp = v[i];
        }
    }
    cout << temp << endl;
    cout << temp2 << endl;
}