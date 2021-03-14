#include <iostream>
using namespace std;

void solution() {
    int input;
    int counter = 0;
    cin >> input;
    if(input <= 3 && input != 2 ) {
        cout << "-1" << endl;
    }
    else {
        int temp_input = input;
        while(true) {
            if(temp_input <= 4) {
                break;
            }
            else {
                counter = counter + temp_input/5;
                temp_input = temp_input%5;
                if(temp_input%2 == 1 && temp_input != 5) {
                    counter--;
                    temp_input = temp_input+5;
                    break;
                }
            }
        }
        while(true) {
            if(temp_input == 0) {
                break;
            }
            else {
                counter = counter + temp_input/2;
                temp_input = temp_input%2;
            }
        }
        cout << counter << endl;
    }
}

int main() {
    solution();
    return 0;
}