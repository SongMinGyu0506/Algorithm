#include <iostream>
#include <set>

using namespace std;

void result() {
    int N;
    set<int> s;
    for (int i = 0; i < 10; i++)
    {
        cin >> N;
        s.insert(N%42);
    }
    cout << s.size() << endl;
}

int main() {
    result();
    return 0;
}