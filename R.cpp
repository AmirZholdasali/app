#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, K;
    cin >> N >> K;
    vector<int> vec;
    for(int i = 1; i<=N; i++){
        vec.push_back(i);
    }

    int result = 0;

    do{
        int P = 0;
        for(int i = 1; i<=N; i++){
            if(i == vec[i-1]){
                P++;
            }
        }

        if(P == K){
            result++;
        }
    }
    while(next_permutation(vec.begin(), vec.end()));

    cout << result;
    return 0;
}