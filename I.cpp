#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> temp1;
    set<int> temp2;
    vector<int> nums;

    while(N--){
        int x;
        cin >> x;
        temp1.push_back(x);
    }

    for(int val : temp1){
        if(temp2.find(val) == temp2.end()){
            nums.push_back(val);
            temp2.insert(val);
        }
    }

    do{
        for(int val : nums){
            cout << val << " ";
        }
        cout << endl;
    }
    while(next_permutation(nums.begin(), nums.end()));

    
    return 0;
}