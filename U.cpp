#include <bits/stdc++.h>
using namespace std;

bool areEqual(vector<int> vec, set<int> sorted){
    auto it = sorted.begin();
    for(int v : vec){
        if(v != *it){
            return false;
        }
        ++it;
    }
    return true;
}

int main(){
    int N;
    cin >> N;
    vector<int> vec;
    set<int> sorted;

    while(N--){
        int x;
        cin >> x;
        vec.push_back(x);
    }

    for(int v : vec){
        sorted.insert(v);
    }

    if(areEqual(vec, sorted)){
        cout << "YES";
        return 0;
    }

    int n = vec.size();
    for(int i = 0; i<n-1 ; i++){
        for(int j = 1; j<n; j++){
            if(j<=i)
                continue;
            else{
                swap(vec[i], vec[j]);
                if(!areEqual(vec, sorted)){
                    swap(vec[i], vec[j]);
                }
                else{
                    cout << "YES";
                    return 0;
                }
            }
        }
    }
    cout << "NO";
    return 0;
}