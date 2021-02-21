#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void print_fnc(int n) {
    cout << n << endl;
}

void solution(vector<int> length) {
    int hunderd;
    for (int i = 0; i < length.size(); i++)
    {
        hunderd = hunderd + length[i];
    }
    for (int i = 0; i < length.size(); i++)
    {
        for (int j = i+1; j < length.size(); j++)
        {
            if(hunderd-length[i]-length[j] == 100) {
                length.erase(length.begin()+i);
                length.erase(length.begin()+j);
            }
        }
    }
    for_each(length.begin(),length.end(),print_fnc);
}

int main() {
    vector<int> length;
    int temp;
    for (int i = 0; i < 9; i++)
    {
        cin >> temp;
        length.push_back(temp);
    }
    stable_sort(length.begin(),length.end());
    solution(length);
    return 0;
}