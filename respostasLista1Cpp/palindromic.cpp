#include <iostream>
#include <sstream>

using namespace std;
bool isPalindromic(int num);

int main(int argc, char const *argv[])
{
    int num1,num2,count = 0;
    string input;
    getline(cin,input);
    istringstream iss(input);

    iss >> num1 >> num2;

    for (int i = num1; i < num2 + 1; i++)
    {
        if (isPalindromic(i))
        {
            count++;
        }
    }
    cout << count << endl;
    return 0;
}

bool isPalindromic(int num){
    string str = to_string(num);
    int size = str.size();

    for (int i = 0; i < size/2; i++)
    {
        if (str[i] != str[size -i -1])
        {
            return false;
        }
    }
    return true;
}
