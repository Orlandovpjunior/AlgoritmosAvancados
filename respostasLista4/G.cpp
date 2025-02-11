#include <iostream>
using namespace std;

int findNumber(long long n);

int main(int argc, char const *argv[])
{
    long long n;
    cin >> n;
    cout << findNumber(n) << endl;

    return 0;
}

int findNumber(long long n){

    int contador = 0;

    if (n == 1)
    {
        return contador = 0;
    }
    else
    {
        while((1LL << contador) <= n){
            contador++;
        }
        contador--;
    }
    return contador;
}
