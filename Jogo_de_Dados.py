import random;

print( '==== Bem Vindo a Jogo de Dados ====')
print('Tente acertar o resultado do lançamento de dois dados')

while True:
    usuario = int(input('Digite um número entre 2 e 12: '))
    if usuario >=2 and usuario <= 12:
     break

print("=== Dados Lançados ===")

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

resultado = (dado1 + dado2)

print('Resultado: ', resultado)

if resultado == usuario:
    print("Voce acertou!")
else:
    print("Voce errou. Tente novamente.")    
