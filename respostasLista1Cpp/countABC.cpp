#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

bool temABC(const string &str, int i);
int contaABC(string str);

int main(int argc, char const *argv[])
{
    int n, q;
    cin >> n >> q;
    string s;
    cin >> s;

    int qtdAbc = contaABC(s);

    for (int i = 0; i < q; i++)
    {
        int pos;
        char letra;
        cin >> pos >> letra;
        pos--;

        for (int j = pos - 2; j <= pos; j++) {
            if (temABC(s, j)) {
                qtdAbc--;
            }
        }
        s[pos] = letra;

        for (int j = pos - 2; j <= pos; j++) {
            if (temABC(s, j)) {
                qtdAbc++;
            }
        }
        cout << qtdAbc << endl;
    }

    return 0;
}

int contaABC(string str){
    int contador = 0;

    for (int i = 0; i < str.size() - 2; i++)
    {
        if (str[i] == 'A' && str[i + 1] == 'B' && str[i + 2] == 'C')
        {
            contador++;
        }
    }

    return contador;
}

bool temABC(const string &str, int i) {
    if (i < 0 || i > str.size() - 3) return false;
    return (str[i] == 'A' && str[i + 1] == 'B' && str[i + 2] == 'C');
}


