#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

bool ehPalindromo(int num){
    string numStr = to_string(num);
    int len = numStr.size();

    for (int i = 0; i < len/2; i++)
    {
        if(numStr[i] != numStr[len - i -1]){
            return false;
        }
    }
    return true;

}

int main(int argc, char const *argv[])
{
    string entrada;
    getline(cin, entrada);
    stringstream ss(entrada);
    vector<int> nums;
    int num;

    while (ss >> num)
    {
        nums.push_back(num);
    }

    int count = 0;
    for (int i = nums[0]; i <= nums[1]; i++)
    {
        if (ehPalindromo(i))
        {
            count++;
        }
    }

    cout << count << endl;
    return 0;
}
