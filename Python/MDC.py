while True:
    n = int(input('Digite um número: '))
    m = int(input('Digite um número maior que o digitado anteriormente: '))
    if n >= m:
        print('Houve algum erro, tente novamente!')
    if m > n:
        break
x = m
y = n
r = x % y
x = y
y = r
while y != 0:
    r = x % y
    x = y
    y = r
print(f'O MDC entre {n} e {m} é {x}')
