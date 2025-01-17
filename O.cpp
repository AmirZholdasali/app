#include <bits/stdc++.h>
using namespace std;

/*
1) vector
2) next_permutation
3) check if it is a polindrome (write a function)
4) output the result
*/

bool isPolindrome(vector<int> vec){
    int n = vec.size();
    int a = 0;
    int b = n-1;
    for(int i = 0; i<n/2; i++){
        if(vec[a+i] != vec[b-i])
            return false;
    }
    return true;
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

    sort(vec.begin(), vec.end());

    while(next_permutation(vec.begin(), vec.end())){
        if(isPolindrome(vec)){
            for(int v : vec){
                cout << v << " ";
            }
            return 0;
        }
    }
    cout << "Impossible";
    return 0;
}