#include <bits/stdc++.h>
using namespace std;

int main(){
    string number;
    cin >> number;

    vector<char> nums;
    for(int i = 0 ; i<number.size(); i++){
        nums.push_back(number[i]);
    }

    for(int i = 0; i< nums.size()-1; i++){
        bool changed = false;
        int root = sqrt( stoi(string(1, nums[i]) + string(1, nums[i+1])) );
        int temp = stoi(string(1, nums[i]) + string(1, nums[i+1]));
        if(root * root == temp){
            changed = true;
            // cout << nums[i] << " is erased" << endl;
            nums.erase(nums.begin() + i);
            // cout << nums[i] << " is erased" << endl;
            nums.erase(nums.begin() + i);
            i = 0;
        }
        if(changed && nums.size() != 0){
            i--;
        }
        if(nums.empty()){
            break;
        }
    }

    if(nums.empty()){
        cout << "Stack is empty";
    } else{
    for(int i = nums.size()-1; i>=0; i--){
        cout << nums[i];
    }}
    return 0;
}