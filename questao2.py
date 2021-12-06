from random import randint


if __name__ == '__main__':
    dados = [0 for _ in range(6)]
    
    umNome = input('Por favor digite o seu nome: ')

    for _ in range(100):
        lancamento = randint(1, 6)
        dados[lancamento - 1] += 1

    for d in range(6):
        print(f"{umNome} o valor {d + 1} apareceu em: {dados[d]} lançamentos! ")
        