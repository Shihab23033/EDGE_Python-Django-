#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    vector<int> a(n),b(n);
    for(int i=0;i<n;i++) {
        cin>>a[i];
    }   
    for(int i=0;i<n;i++) {
        cin>>b[i];
    }
    vector<pair<int,int>> v;
    for(int i=0;i<n;i++) {
        v.push_back({a[i], b[i]});
    }int ans = 0;
    sort(v.begin(), v.end());
    while(v[0].first>= v[0].second){
        ans=0;
        bool flag = true,exit= false;
        for(int i=1;i<n;i++) {
            int tar=(v[i].first-v[0].first);
            if(v[0].first<v[i].second) {
                exit = true;
                break;
            }
            if( tar%v[i].second== 0) {
                ans+= tar/v[i].second;
            } else {
                flag = false;
                break;
            }
        }
        if (exit) {
            cout<<-1<<endl;
            return 0;
        }
        if(flag) {
            cout<<ans<<endl;
            return 0;
        }
        
        v[0].first -= v[0].second;
            
    }
    cout<<-1<<endl;
    return 0;
}