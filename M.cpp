#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;

    for(int i = 1; i<=N; i++){
        vector<int> que(i);
        fill(que.begin(), que.end(), i);

        for(int val : que){
            cout << val << " ";
        }

    }
    return 0;
}