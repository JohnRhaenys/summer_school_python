#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define MAX 50

typedef uint8_t BYTE;

void ler_nome_arquivo(char* nome_arquivo);
void criar_copia_arquivo(FILE* arquivo_original, char* nome_arquivo);
char* gerar_nome_copia(char* nome_arquivo_original);



int main()
{
	char nome_arquivo[MAX];
	ler_nome_arquivo(nome_arquivo);
	
	FILE* arquivo = fopen(nome_arquivo, "r");
	if (arquivo == NULL)
	{
		printf("Erro ao abrir o arquivo!\n");
		return 1;
	}
	
	criar_copia_arquivo(arquivo, nome_arquivo);

	return 0;
}



void ler_nome_arquivo(char* nome_arquivo)
{
	size_t length;
	do
	{
		printf("Insira o nome do arquivo: ");	
		fgets(nome_arquivo, MAX, stdin);
		length = strlen(nome_arquivo);
	}
	while (length == 0 || (length == 1 && nome_arquivo[length - 1] == '\n'));
	
	nome_arquivo[length - 1] = '\0';	
}



void criar_copia_arquivo(FILE* arquivo_original, char* nome_arquivo_original)
{
	char* nome_copia = gerar_nome_copia(nome_arquivo_original);

	// Criando um novo arquivo que sera' a copia da imagem original
	FILE* arquivo_copia = fopen(nome_copia, "w");
	if (arquivo_copia == NULL)
	{
		printf("Erro ao criar a copia do arquivo!\n");
		return;
	}
	
	// Copiando o conteudo da imagem original para a copia
	BYTE buffer;
	while (fread(&buffer, sizeof(BYTE), 1, arquivo_original))
	{
		fwrite(&buffer, sizeof(BYTE), 1, arquivo_copia);
	}
	
	printf("Arquivo \"%s\" copiado com sucesso para (\"%s\")\n", nome_arquivo_original, nome_copia);
	
	// Liberando a memoria alocada, afinal se deu malloc, tem que dar free!
	free(nome_copia);
}




char* gerar_nome_copia(char* nome_arquivo_original)
{
	size_t tam_copia = strlen("_copia");

	// Adicionamos 1 porque precisamos colocar o '\0' no final
	size_t tamanho_nome_novo = strlen(nome_arquivo_original) + tam_copia + 1;
	char* nome_copia = malloc(tamanho_nome_novo * sizeof(char));
	
	int i = 0;
	char c;
	while ((c = nome_arquivo_original[i]) != '.')
	{
		nome_copia[i++] = c;
	}
	int j = i;
		
	strncat(nome_copia, "_copia", tam_copia);
	i += tam_copia;
		
	while ((c = nome_arquivo_original[j]) != '\0')
	{
		nome_copia[i++] = c;
		j++;
	}
	nome_copia[i] = '\0';
	
	return nome_copia;
}
