#include <iostream>
#include <cstring>
using namespace std;

int solution(int counter, int N, int M, bool checker[]) {
    int result = 0;
    if(counter == N) {
        result++;
        return result;
    }
    else {
        for (int i = 0; i < M; i++)
        {
            
        }
    }
}

int main() {
    int test_case;
    int N,M;
    cin >> test_case;
    cin >> N >> M;
    bool checker[M];

    for (int i = 0; i < test_case; i++)
    {
        memset(checker,false,sizeof(checker));
        solution(0,N,M,checker);    
    }
    return 0;
}