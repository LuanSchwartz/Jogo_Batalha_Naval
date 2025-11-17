#🎮 Batalha Naval — Versão Terminal (Python)

#Um jogo clássico de Batalha Naval, totalmente jogável pelo terminal, com cores, sistema de munição, ranking e posicionamento aleatório de embarcações. Desenvolvido em Python.

#📌 Funcionalidades

#🗺️ Tabuleiro 10x15 com coordenadas alfanuméricas

#🚢 4 tipos de embarcações:

#P — Porta-aviões (4 células)

A — Avião (3 células)

N — Navio (2 células)

S — Submarino (1 célula)

🎯 Sistema de munição:

Você começa com 10 tiros

Erro: -1 munição

Acerto: +2 munições

Embarcação afundada: +3 munições

🏆 Ranking automático (arquivo ranking.txt)

🎨 Colorização com Colorama

🔄 Limpeza automática da tela para melhor jogabilidade

🛠️ Tecnologias utilizadas

Python 3.x

Colorama (para cores no terminal)

Instalação da dependência:

pip install colorama

▶️ Como jogar

Clone este repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git


Entre na pasta:

cd seu-repositorio


Execute o jogo:

python batalha_naval.py


No menu inicial, escolha:

1 → Jogar

2 → Ver ranking

3 → Sair

📜 Regras do jogo

Escolha coordenadas usando:

Linhas: 1 a 10

Colunas: A a O

O jogo termina quando:

Todos os navios forem destruídos ou

A munição acabar

🧩 Exemplo de coordenadas

Linha: 5

Coluna: C
→ Tiro em: 5C

🗂️ Estrutura dos arquivos
📦 batalha-naval
 ┣ 📄 batalha_naval.py
 ┣ 📄 ranking.txt (criado automaticamente)
 ┗ 📄 README.md

🏅 Ranking

Após cada jogo finalizado, sua pontuação será salva no arquivo ranking.txt no formato:

NomeDoJogador: X tentativas
