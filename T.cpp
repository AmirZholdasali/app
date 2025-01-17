#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> a;
    while(N--){
        int x;
        cin >> x;
        a.push_back(x);
    }
    int M;
    cin >> M;
    vector<int> b;
    while(M--){
        int x;
        cin >> x;
        b.push_back(x);
    }

    a.insert(a.end(), b.begin(), b.end());

    sort(a.begin(), a.end());

    for(int v : a){
        cout << v << " ";
    }
    return 0;
}