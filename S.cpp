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

    sort(vec.begin(), vec.end());
    vec.erase(unique(vec.begin(), vec.end()), vec.end());

    do{
        for(int v : vec){
            cout << v << " ";
        }
        cout << endl;
    }
    while(next_permutation(vec.begin(), vec.end()));
    return 0;
}