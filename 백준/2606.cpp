/*BaekJoon RUNTIME ERROR Why?*/

#include <iostream>
#include <queue>

using namespace std;

int N, M;
int computer[10][10];
int visited[10];
int counter = 0;
queue<int> q;

int bfs(int start_idx) {
	int temp_counter = 0;
	q.push(start_idx);
	visited[start_idx] = true;

	while (!q.empty()) {
		start_idx = q.front();
		q.pop();

		for (int i = 0; i <= M; i++)
		{
			if (computer[start_idx][i] && !visited[i]) {
				visited[i] = true;
				q.push(i);
				temp_counter++;
			}
		}
	}
	return temp_counter;
}

int main() {
	cin >> N;
	cin >> M;
	for (int i = 0; i < M; i++)
	{
		int start, end;
		cin >> start >> end;
		computer[start][end] = 1;
		computer[end][start] = 1;
	}
	visited[1] = true;
	counter = bfs(1);
	cout << counter << endl;
	return 0;
}