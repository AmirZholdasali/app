#include <bits/stdc++.h>
using namespace std;

struct Translation{
    string word;
    string translation;
};

int main(){
    int N;
    cin >> N;
    Translation t[N];
    for(int i = 0; i<N; i++){
        string x, y;
        cin >> x;
        cin >> y;
        t[i].word = x;
        t[i].translation = y;
    }

    string r;
    cout << "---" << "\n";
    cin >> r;
    for(auto val : t){
        if(r == val.word){
            continue;
        } else{
            cout << val.word << ' ' << val.translation << "\n";
        }
    }
    return 0;
}