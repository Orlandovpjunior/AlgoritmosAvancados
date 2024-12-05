#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
    int n, x;
    cin >> n >> x;
    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    unordered_map<int, int> seen;
    bool achou = false;

    for (int i = 0; i < n; i++) {
        int complement = x - arr[i];
        if (seen.find(complement) != seen.end()) {
            cout << seen[complement] + 1 << " " << i + 1 << endl;
            achou = true;
            break;
        }
        seen[arr[i]] = i;
    }

    if (!achou) {
        cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}
