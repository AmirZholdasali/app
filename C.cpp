#include <bits/stdc++.h>
using namespace std;

struct Grade{
    string name;
    double score;
};

int main(){
    int N;
    cin >> N;
    Grade g[N];
    for(int i = 0; i<N; i++){
        string s;
        double d;
        cin >> s;
        cin >> d;
        g[i].name = s;
        g[i].score = d;
    }

    for(auto val : g){
        cout << val.name << ' ' << val.score << "\n";
    }
    return 0;
}