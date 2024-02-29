import socket
import Conexao

class JogoVelha:
    
    def __init__(self):
        self.tabela = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
        self.inicializador = 'X'
        self.jogador = 'X'
        self.adversario = 'O'
        self.vencedor = None
        self.fim_jogo = False
        self.contador = 0
        self.host = Conexao.HOST
        self.port = Conexao.PORT
    

    def criando_server(self):
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        print(f'SERVER CRIADO COM HOST E PORTA {self.host}/{self.port}\nAGUARDANDO O CLIENTE SE CONECTAR...')
        server.listen(1)
        
        client, endereco = server.accept()
        print(f"CONEXÃO SUCEDIDA PARA O CLIENTE COM PORTA E HOST {endereco[0]}/{endereco[1]}")
        self.jogador = "X"
        self.adversario = "O"

        self.conexao_sucedida(client=client)
        

    def conexao_jogo(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))
        print(f'SERVER CRIADO COM HOST E PORTA {self.host}/{self.port}\nAGUARDANDO O CLIENTE SE CONECTAR...')
        self.jogador = 'O'
        self.adversario = 'X'
        self.conexao_sucedida(client=client)
           
        
    def conexao_sucedida(self, client):
        while not self.fim_jogo:
            if self.inicializador == self.jogador:
                print(f"\n={self.inicializador}= MINHA VEZ DE JOGAR ={self.inicializador}=\n")
                posicao = input('Informe uma posição [LINHA, COLUNA]: ')
                separacao = posicao.split(',')
                
                while True:
                    if  separacao[0] in '012' and separacao[1] in '012':
                        break
                    else:
                        print("Posição Inválida! Digite apenas valores entre 0 e 2 entre vírgula.\nTente novamente...")
                        posicao = input('Informe uma posição [LINHA (0 a 2), COLUNA(0 a 2)]: ')
                        separacao = posicao.split(',')
                        
                if self.checar_posicao(posicao.split(',')):
                    client.send(posicao.encode('utf-8'))
                    self.aplicar_posicao(posicao.split(','), self.jogador)
                    self.inicializador = self.adversario
                else:
                    print("POSIÇÃO INVÁLIDA!\nTente novamente...")
                print("\nAGUARDANDO O ADVERSÁRIO JOGAR...")
            else:
                dado = client.recv(1024)
                if not dado:
                    break
                else:
                    self.aplicar_posicao(dado.decode('utf-8').split(','), self.adversario)
                    self.inicializador = self.jogador
                
        
    
    def aplicar_posicao(self, posicao, jogada):
        self.contador += 1
        self.tabela[int(posicao[0])][int(posicao[1])] = jogada
        self.mostrar_tabela()
        if self.checar_vencedor():
            if self.vencedor == self.jogador:
                print("VOCÊ VENCEU!")
                exit()
            elif self.vencedor == self.adversario:
                print("VOCÊ PERDEU!")
                exit()
            else:
                self.vencedor = None
                print("DEU VELHA!")
                self.fim_jogo = True
                exit()
    
    
    def checar_posicao(self, posicao):
        return self.tabela[int(posicao[0])][int(posicao[1])] == " "
    
    
    def checar_vencedor(self):
        for linha in range(3):
            if self.tabela[linha][0] ==  self.tabela[linha][1] == self.tabela[linha][2] != " ":
                self.vencedor = self.tabela[linha][0]
                self.fim_jogo = True
                return True
        for coluna in range(3):
            if self.tabela[0][coluna] == self.tabela[1][coluna] == self.tabela[2][coluna] != " ":
                self.vencedor = self.tabela[0][coluna]
                self.fim_jogo = True
                return True
        if self.tabela[0][0] == self.tabela[1][1] == self.tabela[2][2] != " ":
            self.vencedor = self.tabela[0][0]
            self.fim_jogo = True
            return True
        if self.tabela[0][2] == self.tabela[1][1] == self.tabela[2][0] != " ":
            self.vencedor == self.tabela[0][2]
            self.fim_jogo = True
        for linha in self.tabela:
            for item in linha:
                if item != " " and self.contador == 9 and self.vencedor == None:
                    self.fim_jogo = True
                    return True
        return False
    
    
    def mostrar_tabela(self):
        print('\n')
        for linha in range(3):
            print(" | ".join(self.tabela[linha]))
            if linha != 2:
                print("-----------")
        print("\n")
                