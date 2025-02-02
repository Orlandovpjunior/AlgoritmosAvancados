#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <bits/stdc++.h>

using namespace std;

int main() {
    string input;
    getline(cin, input);
    istringstream iss(input);
    vector<int> numbers;
    long double soma = 0;
    int num;

    while (iss >> num) {
        numbers.push_back(num);
    }

    for (int i = 0; i < numbers.size(); i++)
    {
        soma += numbers[i] * pow(2,i);
    }

    cout << fixed << setprecision(0) << soma << endl;
    

    return 0;
}
