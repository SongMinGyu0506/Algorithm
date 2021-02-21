#include <iostream>
#include <string>
using namespace std;

int main() {
    string a;
    int N;
    int result_score = 0;
    int score = 1;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> a;
        for (int j = 0; j < a.size(); j++)
        {
            if(a[j] == 'O') {
                result_score = result_score+score;
                score++;
            }
            else {
                score = 1;
            }
        }
        cout << result_score << endl;
        result_score = 0;
        score = 1;
    }
    return 0;
}