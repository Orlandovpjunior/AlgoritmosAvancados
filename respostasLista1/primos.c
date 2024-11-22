#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void geraPrimo (int valor, bool *Ehprimo){
    for (int i = 0; i <= valor; i++) Ehprimo[i] = true;
    
    for (int i = 2; i * i <= valor; i++)
    {
        if (Ehprimo[i])
        {
            for (int j =  i * i; j <= valor; j += i)
            {
                Ehprimo[j] = false;
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    int v;
    scanf("%d", &v);

    bool *ehPrimo =(bool *) malloc((v + 1) * sizeof(ehPrimo));

    geraPrimo(v, ehPrimo);
    int achou = 0;

    for (int i = 2; i <= v/2; i++)    {
        if (ehPrimo[i] && ehPrimo[v - i])
        {
            printf("%d %d\n", i, v - i);
            achou = 1;
            break;
        }
        
    }

    if (!achou)
    {
        printf("%d\n", -1);
    }

    free(ehPrimo);

    return 0;
}