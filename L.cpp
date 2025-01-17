#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> nums;

    while(N--){
        int x;
        cin >> x;
        if(x<0){
            x *= -1;
        }
        nums.push_back(x);
    }

    int countPrime = count_if(nums.begin(), nums.end(), [](int n){
        int cnt = 0;
        if(n == 0 || n == 1)
            return false;
        for(int i = 1; i<=n; i++){
            if(n%i == 0){
                cnt++;
            }
        }
        if(cnt == 2){
            return true;
        }
        else{
            return false;
        }
    });

    cout << countPrime;


    return 0;
}