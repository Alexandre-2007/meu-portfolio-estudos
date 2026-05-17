# Faça um programa que calcule a multiplicação de três números inteiros digitados pelo usuário
def calcula_mult(m1,m2,m3):
    multiplicacao = m1*m2*m3
    return multiplicacao


if __name__ == '__main__':
    m1 = int(input("Valor: "))
    m2 = int(input("Valor: "))
    m3 = int(input("Valor: "))
    calcula_mult(m1,m2,m3)
    print("O resultado é: ",calcula_mult(m1,m2,m3))
