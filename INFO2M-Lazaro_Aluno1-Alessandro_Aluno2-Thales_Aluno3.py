import random

def jogo_forca():
    palavras = ['nike', 'adidas', 'lupo', 'mizuno', 'fila', 'puma', 'umbro', 'penalty']
    palavras_marcas = random.choice(palavras)
    letras_descobertas = []
    chances = 5
    print ('- JOGO DA FORCA -'
    '\n Tema: Marcas esportivas')
    
    while True:
        letra = input("Digite uma letra: " )
        

        if letra in letras_descobertas:
            print("Você já digitou essa letra. Tente novamente.")
            continue
        
        if letra in palavras_marcas:
            letras_descobertas.append(letra)
            if set(palavras_marcas) == set(letras_descobertas):
                print("Parabéns! Você ganhou!")
                break
        else:
            chances -= 1
            print(f"Essa letra não está na palavra. Você tem {chances} chances restantes.")
            
            if chances == 0:
                print(f"Você perdeu! A palavra era {palavras_marcas}")
                break
        if chances==3:
            if palavras_marcas==(palavras[0]):
                print('A DICA É: Esta marca patrocina a seleção brasileira de futebol')
            elif palavras_marcas==(palavras[1]):
                print('A DICA É: Marca custo-benefício do mercado')
            elif palavras_marcas==(palavras[2]):
                print('A DICA É: Marca muito conhecida por suas roupas e máscaras')
            elif palavras_marcas==(palavras[3]):
                print('A DICA É: Seus tênis são muitos usados em festas paulistas')
            elif palavras_marcas==(palavras[4]):
                print('A DICA É: Seus tênis são muito utilizados por jogadores de tênis')
            elif palavras_marcas==(palavras[5]):
                print('A DICA É: Patrocina o ídolo da seleção brasileira')
            elif palavras_marcas==(palavras[6]):
                print('A DICA É: Marca conhecida por patrocinar o maior jogador da história do futsal')
            elif palavras_marcas==(palavras[7]):
                print('A DICA É: Marca conhecida por produzir bolas de todos os tipos de modalidades')
        for letra_palavra in palavras_marcas:
            if letra_palavra in letras_descobertas:
                print(letra_palavra, end=' ')
            else:
                print('_', end=' ')
        print()

jogo_forca()
