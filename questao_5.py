def inverte_string(string):
    # Inicializa uma string vazia para armazenar o resultado da inversão
    string_invertida = ""
    
    # Percorre a string da última posição até a primeira, adicionando os caracteres invertidos à string_invertida
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    
    # Retorna a string invertida
    return string_invertida

# String a ser invertida (pode ser alterada conforme necessário)
minha_string = "Olá, mundo!"

# Chama a função para inverter a string e imprime o resultado
print("String original:", minha_string)
print("String invertida:", inverte_string(minha_string))