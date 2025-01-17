#include <bits/stdc++.h>

using namespace std;

int main() {

    int n, x, mx = INT_MIN;

    map<int, int> mp;

    cin >> n;

    for(int i = 1; i <= n; i++){
        cin >> x;
        mp[x]++;
        mx = max(mx, mp[x]);
    }
    
    if(mx > n / 2 && n - mx == mx-1){
        cout << "Possible";
    }
    else if(mx <= n / 2){
        cout << "Possible";
    }
    else cout << "Impossible";


}