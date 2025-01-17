#include <bits/stdc++.h>
using namespace std;

struct Point{
    int x, y;
};

int main(){
    pair<int, int> start;
    cin >> start.first >> start.second;
    int N;
    cin >> N;
    Point p[N];

    vector<pair<Point, int> > counts;

    for(int i = 0; i<N; i++){
        cin >> p[i].x >> p[i].y;
        int l = sqrt(pow(p[i].x - start.first, 2) + pow(p[i].y - start.second, 2));
        counts.push_back(make_pair(p[i], l));
    }

    sort(counts.begin(), counts.end(), [](const std::pair<Point, int>& a, const std::pair<Point, int>& b){
        return a.second < b.second;
    });

    for(auto val : counts){
        cout << val.first.x << ' ' << val.first.y << "\n";
    }



    return 0;
}