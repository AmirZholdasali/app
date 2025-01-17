#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, M;
    cin >> N >> M;

    vector<int> nums;
    while(N--){
        int x;
        cin >> x;
        nums.push_back(x);
    }

    reverse(nums.begin(), nums.begin() + M);
    reverse(nums.begin()+M, nums.end());

    for(int val : nums){
        cout << val << " ";
    }

    return 0;
}