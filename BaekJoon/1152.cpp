#include <iostream>
#include <string>
using namespace std;

int solution() {
    string input;
    int counter = 1;
    getline(cin, input);

    /*맨 앞뒤 글자 공백확인*/
    if(input[0] == 32) {
        input.erase(input.begin());
    }
    if(input[input.size()-1] == 32) {
        input.erase(input.begin()+(input.size()-1));
    }
    if(input.size() == 0) {
        counter = 0;
    }

    /*단어 카운터*/
    for (int i = 0; i < input.size(); i++)
    {
        char temp = input[i];
        if(temp == 32) {
            counter++;
        }
    }
    return counter;
}

int main() {
    cout << solution() << endl;
    return 0;
}