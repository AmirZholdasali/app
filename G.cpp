#include <bits/stdc++.h>
using namespace std;

int main(){
    stack<int> stk;
    for(int i = 0; i<5; i++){
        int x;
        cin >> x;
        stk.push(x);
    }
    cout << "---" << "\n";
    for(int i = 0; i<2; i++){
        stk.pop();
    }

    while(!stk.empty()){
        cout << stk.top() << ' ';
        stk.pop();
    }
    return 0;
}