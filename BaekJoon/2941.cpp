#include <iostream>
#include <string>
using namespace std;

void solution() {
    int counter = 0;
    string input;
    cin >> input;
    for (int i = 0; i < input.size(); i++)
    {
        if(input[i] == NULL) {
            break;    
        }
        if(input[i+1] == NULL) {
            counter++;
        }

        else if(input[i] == 'c' ) {
            if(input[i+1] == '=') {
                counter++;
                i++;
            }
            else if(input[i+1] == '-') {
                counter++;
                i++;
            }
            else {
                counter++;
            }
        }

        else if(input[i] == 'd') {
            if(input[i+1] == 'z') {
                if(input[i+2] == '=') {
                    counter++;
                    i++;
                    i++;
                }
                else {
                    counter++;
                }
            }
            else if(input[i+1] == '-') {
                counter++;
                i++;
            }
            else {
                counter++;
            }
        }
        
        else if(input[i] == 'l') {
            if(input[i+1] == 'j') {
                counter++;
                i++;
            }
            else { counter ++;}
        }
        else if(input[i] == 'n') {
            if(input[i+1] == 'j') {
                counter++;
                i++;
            }
            else {counter++;}
        }
        else if(input[i] == 's') {
            if(input[i+1] == '=') {
                counter++;
                i++;
            }
            else {
                counter++;
            }
        }
        else if(input[i] == 'z') {
            if(input[i+1] == '=') {
                counter++;
                i++;
            }
            else {
                counter++;
            }
        }
        else {
            counter++;
        }
    }
    cout << counter << endl;
}

int main() {
    solution();
    return 0;
}