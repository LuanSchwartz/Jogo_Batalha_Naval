import random
import os
from colorama import Fore, Style, init

init(autoreset=True)

def criar_tabuleiro(tamanho):
    return [['~' for _ in range(tamanho)] for _ in range(10)]

def imprimir_tabuleiro(tabuleiro, ocultar_navios=True):
    tamanho = len(tabuleiro[0])
    colunas = "ABCDEFGHIJKLMNO"[:tamanho]
    print("  " + " ".join(colunas))
    for i, linha in enumerate(tabuleiro, start=1):
        linha_visivel = [
            Fore.GREEN + "X" + Style.RESET_ALL if celula == "X" else
            Fore.CYAN + "*" + Style.RESET_ALL if celula == "*" else
            "~" if ocultar_navios and celula in "SNAP" else
            celula
            for celula in linha
        ]
        print(f"{i:2} " + " ".join(linha_visivel))

def posicionar_navio(tabuleiro, tamanho, simbolo):
    direcao = random.choice(["H", "V"])
    tamanho_tabuleiro = len(tabuleiro)
    while True:
        if direcao == "H":
            linha = random.randint(0, tamanho_tabuleiro - 1)
            coluna = random.randint(0, len(tabuleiro[0]) - tamanho)
            if all(tabuleiro[linha][coluna + i] == '~' for i in range(tamanho)):
                for i in range(tamanho):
                    tabuleiro[linha][coluna + i] = simbolo
                break
        else:  # Vertical
            linha = random.randint(0, tamanho_tabuleiro - tamanho)
            coluna = random.randint(0, len(tabuleiro[0]) - 1)
            if all(tabuleiro[linha + i][coluna] == '~' for i in range(tamanho)):
                for i in range(tamanho):
                    tabuleiro[linha + i][coluna] = simbolo
                break

def posicionar_embarcacoes(tabuleiro):
    posicionar_navio(tabuleiro, 4, "P")  # Porta-aviões
    posicionar_navio(tabuleiro, 3, "A")  # Avião
    posicionar_navio(tabuleiro, 2, "N")  # Navio
    posicionar_navio(tabuleiro, 1, "S")  # Submarino

def dar_tiro(tabuleiro, linha, coluna, municao):
    if tabuleiro[linha][coluna] in "SNAP":
        simbolo = tabuleiro[linha][coluna]
        tabuleiro[linha][coluna] = "X"
        print(Fore.GREEN + "Você acertou um navio! +2 munições." + Style.RESET_ALL)
        municao += 2
        if not any(simbolo in linha for linha in tabuleiro):
            print(Fore.CYAN + f"Você afundou um {simbolo}! +3 munições." + Style.RESET_ALL)
            municao += 3
        return municao
    elif tabuleiro[linha][coluna] == "~":
        tabuleiro[linha][coluna] = "*"
        print(Fore.CYAN + "Você errou! -1 munição." + Style.RESET_ALL)
        municao -= 1
    else:
        print(Fore.YELLOW + "Você já atirou aqui! Tente outra coordenada." + Style.RESET_ALL)
    return municao

def verificar_fim(tabuleiro):
    for linha in tabuleiro:
        if any(celula in "SNAP" for celula in linha):
            return False
    return True

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_regras():
    limpar_tela()
    print(Fore.CYAN + "Bem-vindo ao jogo de Batalha Naval!")
    print("\nRegras do jogo:")
    print("1. O tabuleiro é uma grade de 10x15, com linhas numeradas e colunas com letras.")
    print("2. Você começa com 10 munições.")
    print("3. Cada tiro consome 1 munição.")
    print("4. Cada acerto adiciona +2 munições.")
    print("5. Cada objetivo afundado adiciona +3 munições.")
    print("6. O jogo termina quando todos os navios forem destruídos ou a munição acabar.")
    print("\nBoa sorte!" + Style.RESET_ALL)
    input("\nPressione Enter para começar o jogo...")

def salvar_pontuacao(nome, tentativas):
    with open("ranking.txt", "a") as arquivo:
        arquivo.write(f"{nome}: {tentativas} tentativas\n")

def exibir_ranking():
    limpar_tela()
    print(Fore.MAGENTA + "Ranking dos Jogadores:")
    try:
        with open("ranking.txt", "r") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Nenhum ranking encontrado. Jogue para criar um ranking!")
    input("\nPressione Enter para voltar ao menu...")

def jogar():
    tamanho = 15
    municao = 10

    tabuleiro = criar_tabuleiro(tamanho)
    posicionar_embarcacoes(tabuleiro)

    mostrar_regras()

    nome = input(Fore.YELLOW + "Digite seu nome: " + Style.RESET_ALL)
    tentativas = 0

    while municao > 0 and not verificar_fim(tabuleiro):
        limpar_tela()
        print(Fore.CYAN + f"Munição restante: {municao}")
        imprimir_tabuleiro(tabuleiro)

        try:
            linha = int(input(Fore.YELLOW + "Digite a linha (1-10): " + Style.RESET_ALL)) - 1
            coluna = input(Fore.YELLOW + "Digite a coluna (A-O): " + Style.RESET_ALL).upper()
            coluna = ord(coluna) - ord("A")
            if 0 <= linha < 10 and 0 <= coluna < tamanho:
                municao = dar_tiro(tabuleiro, linha, coluna, municao)
                tentativas += 1
            else:
                print(Fore.RED + "Coordenadas inválidas. Tente novamente." + Style.RESET_ALL)
        except (ValueError, IndexError):
            print(Fore.RED + "Entrada inválida. Por favor, insira uma linha e uma coluna válidas." + Style.RESET_ALL)

        input("\nPressione Enter para continuar...")

    limpar_tela()
    if verificar_fim(tabuleiro):
        print(Fore.GREEN + "Parabéns! Você destruiu todos os navios!")
    else:
        print(Fore.RED + "Fim de jogo! Você ficou sem munição.")
    print("Tabuleiro final:")
    imprimir_tabuleiro(tabuleiro, ocultar_navios=False)

    salvar_pontuacao(nome, tentativas)

def menu():
    while True:
        limpar_tela()
        print(Fore.CYAN + "=== Batalha Naval ===")
        print("1. Jogar")
        print("2. Exibir Ranking")
        print("3. Sair")
        opcao = input(Fore.YELLOW + "Escolha uma opção: " + Style.RESET_ALL)

        if opcao == "1":
            jogar()
        elif opcao == "2":
            exibir_ranking()
        elif opcao == "3":
            print(Fore.GREEN + "Saindo do jogo. Até a próxima!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente." + Style.RESET_ALL)
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    menu()