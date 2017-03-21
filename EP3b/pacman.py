"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Leonardo Calasans
  NUSP : 9835800
  Turma: 07
  Prof.: Carlos E. Ferreira

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""

# as constantes que podem ser usadas estão em constantes.py
# para usá-las não é necessário escrever "constantes."
from constantes import * 

# os métodos da classe Labirinto poderão ser usados:
#    dimensao(), get(), put(), direcoes_possiveis(), matriz(), ... 
from labirinto import *

# descomente a linha a seguir se você usa alguma função do módulo extras
import extras

#-----------------------------------------------------------------
class Pacman():
    '''Classe utilizada para representar Pac-Mans.

    Cada objeto desta classe tem 6 atributos de estado: 
       `lin`, `col`, `dir`, `pts`, `vidas` e `lab`:

        * `lin` e `col`: inteiros que indicam a posição [lin][col] 
              do Pac-Man;

        * `dir`: caractere (= str) em 'wasdp' que indica a direção 
              do último movimento do Pac-Man.
              Inicialmente é 'p' (= PARADO).
 
        * `pts`: inteiro que indica o número de pac-dots comidos 
              pelo Pac-Man. 
              Inicialmente esse valor é zero.

        * `vidas`: inteiro que indica o número de vidas que restam ao
              Pac-Man. 
              Inicialmente esse valor é três.

        * `lab`: referência (apelido) para um objeto da classe
               Labirinto que representa o labirinto do jogo.
               Cada posição do labirinto contém um dos caracteres
               em CARACTERES_LABIRINTO (= '+. ').
    '''

    #--------------------------------------------------------------
    def __init__(self, lin, col, lab):
        '''(Pacman, int, int, Labirinto) -> None

        Construtor: recebe inteiros `lin`, `col` e referências/apelidos: 

            - `self`: para o objeto Pacman que está sendo construído e
            - `lab` : para um objeto da classe Labirinto.

        O método cria e retorna um objeto que representa um Pac-Man. 

        O Pac-Man criado ocupa a posição [lin][col] do labirinto e
            otem 0 pontos  

        Inicialmente a sua direção é 'p' (= PARADO) e o número de 
            vidas é três.

        Atenção: self.lab deve ser um apelido do parâmetro lab e 
            __não__ um clone.

        Método mágico/especial: usado pelo Python quando criamos
            escrevemos Pacman(). Não tem `return`.
        '''
        #print("Vixe! Ainda não fiz o método Pacman.__init__() :-(")
        self.lin = lin
        self.col = col
        self.pts = 0
        self.dir = 'p'
        self.vidas = 3
        self.labirinto = lab
        print("Pacman.__init__(): criado Pacman: posição [%d][%d], direção '%s', pontos %d, vidas %d"%(self.lin,self.col,self.dir,self.pts,self.vidas))
    #--------------------------------------------------------------        
    def __str__(self):
        '''(Pacman) -> str

        Recebe um Pacman referenciado por `self` e constrói e retorna 
        o string com infomações sobre o Pac-Man.

        Método mágico/especial: usado pelo Python quando utilizamos 
            print() para exibir informações sobre o Pac-Man.
            Esse também é o string retornado pela função nativa str().
        '''
     
        string = "Pacman : posição [%d][%d], direção '%s', pontos %d, vidas %d"%(self.lin, self.col, self.dir, self.pts, self.vidas)
        
        return string 
    
    #--------------------------------------------------------------
    def posicao(self):
        '''(Pacman) -> int, int

        Recebe um Pacman referenciado por `self` e retorna dois inteiros 
        lin e col tais que o Pac-Man está na posição [lin][col].
        '''
        #print("Vixe! Ainda não fiz o método Pacman.posicao() :-(")
        lin = self.lin
        col = self.col
        
        return lin, col
        
    #--------------------------------------------------------------
    def direcao(self):
        '''(Pacman) -> str

        Recebe um Pacman referenciado por `self` e retorna um string
        representando a direção do último movimento do Pac-Man.
        '''
        #print("Vixe! Ainda não fiz o método Pacman.direcao() :-(")
        direção = '%s'%(self.dir)
        return direção

    #--------------------------------------------------------------
    def pontos(self):
        '''(Pacman) -> int

        Recebe um Pacman referenciado por `self` e retorna o 
        número de pacdots comidos (= pontos) pelo Pac-Man.
        '''
        #print("Vixe! Ainda não fiz o método Pacman.pontos() :-(")    
        pontos = self.pts
        return pontos
        
    #--------------------------------------------------------------
    def no_vidas(self):
        '''(Pacman) -> int

        Recebe um Pacman referenciado por `self` e retorna 
        o número de vidas que restam ao Pac-Man.
        '''
        #print("Vixe! Ainda não fiz o método Pacman.no_vidas() :-(")
        vidas = self.vidas
        return vidas
    #--------------------------------------------------------------
    def morra(self):
        '''(Pacman) -> None

        Recebe um Pacman referenciado por `self` e diminui de uma vida
        o número de vidas que restam ao Pac-Man.
        '''
        #print("Vixe! Ainda não fiz o método Pacman.morra() :-(")
        self.vidas = self.vidas - 1
        
    #--------------------------------------------------------------
    def reposicione(self, lin, col):
        '''(Pacman) -> None

        Recebe um Pacman referenciado por `self` e inteiros `lin` e
        `col` e reposiciona o Pac-Man na posição [lin][col].

        Pré-condição: o método supõe que a posicão [lin][col] do labirinto
            contém VAZIO. Isso não precisa ser verificado.
        '''
        #print("Vixe! Ainda não fiz o método Pacman.reposicione() :-(")
        self.lin = lin
        self.col = col
    #--------------------------------------------------------------
    def mova(self, direcao):
        '''(Pacman, str) -> None

        Recebe um Pacman referenciado por `self` e um string `direcao` 
        representando uma direção e, se possível, move o Pac-Man na 
        direção dada, atualizando seus pontos e o labirinto se necessário.
 
        O método imprime uma mensagem indicando se o movimento é possível
        ou não. Se o movimento é possível o método deve imprimir uma
        uma mensagem indicando qual foi o movimento. 

        Veja as mensagens no roteiro.
        
        Sugestão: inspire-se na sua função movimentaPacMan() do EP2.
        '''
        #print("Vixe! Ainda não fiz o método Pacman.mova() :-(")    
        self.dir = direcao
        andou = False
        labirinto = self.labirinto
        lin_anterior = self.lin
        col_anterior = self.col
        matriz_labirinto = labirinto.lab
            
        #Se for pra CIMA:
        if direcao == 'w':
            lin = extras.cic(self.lin - 1, len(matriz_labirinto))
            col = extras.cic(self.col, len(matriz_labirinto[1]))
            if matriz_labirinto[lin][col] == PAREDE:
                print('Pacman.mova(): movimento do Pac-Man de [%d][%d] para [%d][%d] não é possível'%(lin_anterior,col_anterior,lin,col))
                print('Pacman.mova(): Pac-Man continuou na posição [%d][%d]'%(lin_anterior,col_anterior))
            if matriz_labirinto[lin][col] == PACDOT:
                self.pts = self.pts + 1
                matriz_labirinto[lin][col] = VAZIO
                labirinto.pacdots = labirinto.pacdots - 1
                andou = True
            if matriz_labirinto[lin][col] == VAZIO:
                andou = True
       
       #Se for pra DIREITA
        if direcao == 'd':
            lin = extras.cic(self.lin, len(matriz_labirinto))
            col = extras.cic(self.col + 1, len(matriz_labirinto[1]))
            if matriz_labirinto[lin][col] == PAREDE:
                print('Pacman.mova(): movimento do Pac-Man de [%d][%d] para [%d][%d] não é possível'%(lin_anterior,col_anterior,lin,col))
                print('Pacman.mova(): Pac-Man continuou na posição [%d][%d]'%(lin_anterior,col_anterior))
            if matriz_labirinto[lin][col] == PACDOT:
                self.pts = self.pts + 1
                matriz_labirinto[lin][col] = VAZIO
                labirinto.pacdots = labirinto.pacdots - 1
                andou = True
            if matriz_labirinto[lin][col] == VAZIO:
                andou = True
       
       #Se for pra BAIXO       
        if direcao == 's':
            lin = extras.cic(self.lin + 1, len(matriz_labirinto))
            col = extras.cic(self.col, len(matriz_labirinto[1]))
            if matriz_labirinto[lin][col] == PAREDE:
                print('Pacman.mova(): movimento do Pac-Man de [%d][%d] para [%d][%d] não é possível'%(lin_anterior,col_anterior,lin,col))
                print('Pacman.mova(): Pac-Man continuou na posição [%d][%d]'%(lin_anterior,col_anterior))
            if matriz_labirinto[lin][col] == PACDOT:
                self.pts = self.pts + 1
                matriz_labirinto[lin][col] = VAZIO
                labirinto.pacdots = labirinto.pacdots - 1
                andou = True
            if matriz_labirinto[lin][col] == VAZIO:
                andou = True
        
        #Se for pra ESQUERDA
        if direcao == 'a':
            lin = extras.cic(self.lin, len(matriz_labirinto))
            col = extras.cic(self.col - 1, len(matriz_labirinto[1]))
            if matriz_labirinto[lin][col] == PAREDE:
                print('Pacman.mova(): movimento do Pac-Man de [%d][%d] para [%d][%d] não é possível'%(lin_anterior,col_anterior,lin,col))
                print('Pacman.mova(): Pac-Man continuou na posição [%d][%d]'%(lin_anterior,col_anterior))
            if matriz_labirinto[lin][col] == PACDOT:
                self.pts = self.pts + 1
                matriz_labirinto[lin][col] = VAZIO
                labirinto.pacdots = labirinto.pacdots - 1
                andou = True
            if matriz_labirinto[lin][col] == VAZIO:
                andou = True
                
        if andou == True :
            print('Pacman.mova(): Pac-Man moveu-se de [%d][%d] para [%d][%d]'%(lin_anterior,col_anterior, lin, col))
            self.lin = lin    
            self.col = col 
        
        labirinto.lab = matriz_labirinto
        self.labirinto = labirinto
        