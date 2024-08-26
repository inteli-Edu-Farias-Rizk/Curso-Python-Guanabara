import random
from os import name, system

# Função para limpar a tela do console
def limpa_tela():
    if name == 'nt':
        _ = system('cls')  # Windows
    else:
        _ = system('clear')  # Mac/Linux

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Hangman:
    palavras = ['uva', 'melancia', 'mamao']
    jogoRolando = True

    # Método Construtor
    def __init__(self):
        self.vidas = 6
        self.palavra = random.choice(Hangman.palavras)
        self.tamanho = ["_" for letter in self.palavra]
        self.letrasErradas = []

    # Método para adivinhar a letra
    def adivinha(self):

        print('Bem vindo ao jogo da forca')
        print('Advinhe a palavra abaixo: ')
        self.iteracao()
        print(f"\nChances restantes: {self.vidas}")
        print(f"As letras tentadas foram: {', '.join(self.letrasErradas)}")
        tentativa = input("Tente uma letra: ").strip().lower()[0]
        if tentativa in self.palavra:
            posicao = [i for i, v in enumerate(self.palavra) if v == tentativa]
            for indx in posicao:
                self.tamanho[indx] = tentativa
        else:
            if tentativa not in self.letrasErradas:
                self.letrasErradas.append(tentativa)
                self.vidas -= 1

    # Método para verificar se o jogo terminou
    def terminou(self):
        if self.vidas == 0:
            print(f"Você perdeu! A palavra era: {self.palavra}")
            Hangman.jogoRolando = False

    # Método para verificar se o jogador venceu
    def venceu(self):
        if "_" not in self.tamanho:
            print(f"Parabéns! Você acertou a palavra: {''.join(self.tamanho)}")
            Hangman.jogoRolando = False

    # Método para não mostrar a letra no board
    def iteracao(self):
        print(' '.join(self.tamanho))

    # Método para checar o status do game e imprimir o board na tela
    def status(self):
        print(board[6 - self.vidas])

# Instancia o objeto e chama o método para iniciar o jogo
jogo1 = Hangman()

# Loop principal do jogo
while Hangman.jogoRolando:
    jogo1.adivinha()
    jogo1.terminou()
    jogo1.venceu()
    jogo1.status()
