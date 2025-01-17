#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> vec;
    while(N--){
        int x;
        cin >> x;
        vec.push_back(x);
    }

    vec.erase(unique(vec.begin(), vec.end()), vec.end());

    for(int v : vec){
        cout << v << " ";
    }
    return 0;
}