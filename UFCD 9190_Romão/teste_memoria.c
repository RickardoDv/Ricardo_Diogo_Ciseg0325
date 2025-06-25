#include <stdio.h>
#include <string.h>

int main(){

    char nome[10];
    char apelido[10];

    printf("Inserir nome: \n");
    //gets(nome);
    scanf("%s", &nome);
    printf("Inserir Apelido: \n");
    scanf("%s", &apelido);

    
    printf("Escreveu o nome: %s \n ", nome);
    printf("Escreveu o apelido: %s\n", apelido);

    return 0;





}