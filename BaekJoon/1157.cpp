#include <iostream>
#include <string>
#include <vector>
using namespace std;

void solution() {
    string input;
    vector<int> v (26,-1);
    int temp = 0;
    int temp2 = 0;
    char result;

    cin >> input;

    for (int i = 0; i < input.size(); i++)
    {
        if(input[i] <= 90 ) {
            if(v[input[i]-65] == -1) {
                v[input[i]-65] = 0;
                v[input[i]-65]++;
            } else v[input[i]-65]++;
        }
        else {
            if(v[input[i]-97] == -1) {
                v[input[i]-97] = 0;
                v[input[i]-97]++;
            } else v[input[i]-97]++;
        }
    }
    
    for (int i = 0; i < v.size(); i++)
    {
        if(temp2 < v[i]) {
            temp = i;
            temp2 = v[i];
            v[i] = NULL;
        } 
    }
    for (int i = 0; i < v.size(); i++)
    {
        if(temp2 == v[i]) {
            result = '?';
            break;
        }
        result = temp+65;
    }
    cout << result << endl;
}

int main() {
    solution();
    return 0;
}