#include <iostream>
#include <string>
#include <vector>
using namespace std;

void solution() {
    int result = 0;
    string input;
    vector<string> v(12);
    v[3] = "ABC";
    v[4] = "DEF";
    v[5] = "GHI";
    v[6] = "JKL";
    v[7] = "MNO";
    v[8] = "PQRS";
    v[9] = "TUV";
    v[10] = "WXYZ";

    cin >> input;
    for (int i = 0; i < input.size(); i++)
    {
        for (int j = 0; j < v.size(); j++)
        {
            for (int x = 0; x < v[j].size(); x++)
            {
                if(v[j][x] == input[i]) {
                    result = result + j;
                }
            }
        }
    }
    cout << result << endl;
}

int main() {
    solution();
    return 0;
}