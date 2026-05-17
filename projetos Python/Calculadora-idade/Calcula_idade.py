def calcula_idade(ano):
    idade = 2026 - ano
    return idade


if __name__ == '__main__':
    ano = int(input("digite o ano de nascimento: "))
    calcula_idade(ano)
    print("você tem",calcula_idade(ano),"anos")