#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main(int argc, char const *argv[])
{
    int tamanho, consultas;
    

    cin >> tamanho >> consultas;

    string entradaStr;
    int num;
    stringstream ss (entradaStr);
    vector<int> vetor(tamanho);
    
    while (ss >> num)
    {
        vetor.push_back(num);
    }
    

    for (int n : vetor)
    {
        cout << n << " " << endl;
    }


    return 0;
}
