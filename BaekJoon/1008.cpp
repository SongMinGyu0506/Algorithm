#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	double input1;
	double input2;
	cin >> input1 >> input2;
	double result = input1 / input2;
	printf("%.12f\n", result);
	return 0;
}