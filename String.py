def string(palavra):
    letra = 'a'
    qtd = palavra.count(letra)
    print(f'A palavra {palavra} possui {qtd} de a(s)')

palavra = string(input('Digite uma palavra: '))