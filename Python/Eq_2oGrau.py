import math
from time import sleep
print('Equação do 2º grau (genérica): ax² + bx + c ')
print('-=-' * 30) #Efeito visual
while True: #Aqui inicia-se um loop para verificar as exceções(se a = 0 e/ou Delta < 0)
    a = int(input('Digite o valor de a: '))
    if a == 0: #Caso seja a = 0, o que não pode, ele irá perguntar novamente um valor para "a"
        print('O valor de a não pode ser 0 ')
    else: #Caso "a" seja diferente de 0, ele prosseguirá
        b = int(input('Digite o valor de b: '))
        c = int(input('Digite o valor de c: '))
        delta = b * b - 4 * a * c #Fórmula do Delta
        if delta >= 0: #Caso o Delta seja maior ou igual a 0, ele sairá do loop e seguirá o processo corretamente
            break
        else: #Caso contrário, ele reiniciará o loop, perguntado os valores de a, b e c novamente
            print('O valor do Delta deu negativo, portanto, não possui raiz no conjunto dos Reais! ')
x1 = (-b + math.sqrt(delta)) / (2 * a) #Fórmula de Bhaskara
x2 = (-b - math.sqrt(delta)) / (2 * a) #Fórmula de Bhaskara
raizes = [x1, x2] #Lista para poder colocar o Conjunto Solução em ordem ao final do programa(linha 32)
print('-=-' * 30) #Efeito visual
print(f'''Equação do 2º grau (com os valores digitados):
{a}x² + {b}x + {c} ''')
print('-=-' * 30) #Efeito visual
sleep(4) #Temporizador para dar um efeito
print('Calculando o valor do Delta e suas raízes... ')
print('-=-' * 30) #Efeito visual
sleep(4) #Temporizador para dar um efeito
print(f'O valor do Delta é {delta} ')
print(f'O valor de uma das raízes é {x1:.2f} ')
print(f'O valor da outra raíz é {x2:.2f} ')
print('-=-' * 30)
print(f'Conjunto Solução(S) = {[round(r, 2) for r in sorted(raizes)]}') #Valores com 2 casas após a vírgula e em ordem crescente
