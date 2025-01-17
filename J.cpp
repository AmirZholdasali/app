#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> orig;

    while(N--){
        int x;
        cin >> x;
        orig.push_back(x);
    }

    vector<int> ref;
    for(int i = orig.size()-1 ; i>=0; i--){
        ref.push_back(orig[i]);
    }

    for(int i = 0; i<orig.size(); i++){
        if(orig[i] == ref[i]){
            cout << "OK" << endl;
        }
        else if(orig[i] != ref[i]){
            cout << "Instead of " << orig[i] << " here was " << ref[i] << endl;
        }
    }
    return 0;
}