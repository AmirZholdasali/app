#include <bits/stdc++.h>
using namespace std;

int main(){
    string str;
    cin >> str;
    cout << "The anagram variants for string " << str << " are:" << endl;
    sort(str.begin(), str.end());
    cout << str << endl;
    while(next_permutation(str.begin(), str.end())){
        cout << str << endl;
    }
    return 0;
}