#include <stdio.h>

int main(int argc, char const *argv[])
{
    int menor = 0;
    int n, m;

    scanf("%d %d", &n,&m);

    if (n < m)
    {
        menor = n;
    }else if(m < n)
    {
        menor = m;
    }else{
        menor = n;
    }

    if (menor % 2 == 0)
    {
        printf("%s\n", "Malvika");
    }else{
        printf("%s\n", "Akshat");
    }

    return 0;
}
