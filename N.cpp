#include <bits/stdc++.h>
using namespace std;

int main(){
    int A, B;
    cin >> A >> B;
    vector<int> a;
    vector<int> b;
    while(A--){
        int x;
        cin >> x;
        a.push_back(x);
    }
    while(B--){
        int x;
        cin >> x;
        b.push_back(x);
    }

    a.erase(unique(a.begin(), a.end()), a.end());
    b.erase(unique(b.begin(), b.end()), b.end());
    // //==========
    // for(int v : a){
    //     cout << v << " ";
    // }
    // cout << endl;
    // for(int v : b){
    //     cout << v << " ";
    // }
    // cout << endl;
    // //===========

    vector<int> r;
    size_t minsize = min(a.size(), b.size());
    for(int i = 0; i<minsize; i++){
        r.push_back(a[i]);
        r.push_back(b[i]);
    }
    if(a.size() > b.size()){
        r.push_back(a.back());
    }
    else if(b.size() > a.size()){
        r.push_back(b.back());
    }

    // //=============
    // for(int v : r){
    //     cout << v << " ";
    // }
    // cout << endl;
    // //==============

    r.erase(unique(r.begin(), r.end()), r.end());

    for(int val : r){
        cout << val << " ";
    }
    return 0;
}