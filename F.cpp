#include <bits/stdc++.h>
using namespace std;

int main(){
    map<string, pair<double, int> > mp;
    vector<pair<string, double>> v;
    int n;
    cin >> n;
    string s;
    double d;

    for(int i = 0; i<n; i++){
        cin >> s >> d;
        mp[s].first += d;
        mp[s].second++;
    }

    for(auto& entry : mp){
        string name = entry.first;
        double avgGPA = entry.second.first/entry.second.second;
        v.push_back({name, avgGPA});
    }

    sort(v.begin(), v.end(), [](const pair<string, double>& a, const pair<string, double>& b){
        if(a.second != b.second){
            return a.second > b.second;
        }
        return a.first < b.first;
    });

    for(const auto& val : v){
        cout << val.first << ": ";
        printf("%.3f", val.second);
        cout << "\n";
    }
    return 0;
}