#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double A,B,V;
    cin >> A >> B >> V;
    double result = double((V-1)/(A-B));
    result = ceil(result);

    //result = (int)result;
    printf("%.0f\n",result);
}