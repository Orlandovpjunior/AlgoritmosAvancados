#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

void pre_calc() {
    // Função para pré-cálculos (se necessário).
}

void solve() {
    int n;
    cin >> n;

    priority_queue<pair<int, int>> pq;
    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        if (x > 0) pq.push({x, i});
    }

    vector<pair<int, int>> ans;
    while (pq.size() > 1) {
        auto f = pq.top();
        pq.pop();
        auto s = pq.top();
        pq.pop();

        ans.push_back({f.second, s.second});
        f.first--;
        s.first--;

        if (f.first > 0) pq.push(f);
        if (s.first > 0) pq.push(s);
    }

    cout << ans.size() << '\n';
    for (auto i : ans) cout << i.first << " " << i.second << "\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cout << fixed;
    cout.precision(10);

    // freopen("timber_input.txt", "r", stdin);
    // freopen("timber_output.txt", "w", stdout);

    pre_calc();

    int t = 1;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        // cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
