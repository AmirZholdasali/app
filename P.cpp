#include <bits/stdc++.h>
using namespace std;

void toBinary(int value){
    vector<int> v;
    while(value>0){
        v.push_back(value % 2);
        value /= 2;
    }
    reverse(v.begin(), v.end());
    for(int val : v){
        cout << val;
    }
    cout << endl;
}

int main(){
    int N;
    cin >> N;
    vector<int> vec;
    while(N--){
        int x;
        cin >> x;
        vec.push_back(x);
    }

    for_each(vec.begin(), vec.end(), toBinary);
    return 0;
}