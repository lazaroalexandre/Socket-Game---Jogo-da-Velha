# Socket-Game---Jogo-da-Velha

    Jogo da velha usando sockets

# Execução

    Caso você queira testar o jogo sozinho, primeiramente execute
    o arquivo Jogador.py em um terminal e depois o arquivo Adversario.py
    em outro terminal. 
    
    Exemplo:
    - Terminal 1:
        python3 Jogador.py
    - Terminal 2:
        python3 Adversario.py 


    Caso você queira jogar com o outra pessoa em máquinas diferentes, mas na
    mesma rede, basta você copiar o ipv4 da máquina que será executada o Jogador.py
    e subistitir na variável HOST em Conexao.py.

    Exemplo:
    - Terminal:
        ipconfig
        ou
        ifconfig
    - Copiar o ipv4 da máquina
    - Colar no HOST em Conexao.py
    - Copiar o diretório Socket-Game---Jogo-da-Velha já modificado
    - Colar na outra máquina

    - Terminal do Jogador:
        python3 Jogador.py
    - Terminal do Adversário:
        python3 Adversario.py 
