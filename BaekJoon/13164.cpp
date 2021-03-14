#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int i, int j) {
    return j < i;
}

int main() {
    int result = 0;
    int temp;
    int N, K;
    cin >> N >> K;
    vector<int> input_list;
    vector<int> cal_list;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        input_list.push_back(temp);
    }
   for (int i = 0; i < N-1; i++)
   {
       cal_list.push_back(input_list[i+1]-input_list[i]);
   }
   sort(cal_list.begin(),cal_list.end(),compare); //왜 오름차순에서 작은거 두개쓰는건 오류가 먹히는가?
   for (int i = K-1; i < N-1; i++)
   {
       result = result+cal_list[i];
   }
   printf("%d\n",result);
    return 0;
}