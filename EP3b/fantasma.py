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
#    dimensao(), get(), put(), direcoes_possiveis(), ... 
from labirinto import *

# módulo para definição da semente para sorteio dos números pseudo
# aleatórios; usada para sortear um movimento possível para um fantasma
import random # random.randrange(), random.choice() 

# descomente a linha a seguir se você usa alguma função do módulo extras
import extras

#----------------------------------------------------------------------
class Fantasma:
    ''' Classe utilizada para representar um fantasma.

    Cada objeto desta classe tem 4 atributos de estado:
       `lin`, `col`, `direcao` e `lab`:

       * `lin` e `col`: inteiros que indicam a posição [lin][col] 
             do fantasma; 

       * `dir`: caractere (= str) em 'wasd' que indica a direção
             do último movimento do fantasma.

       * `lab`: referência (apelido) para um objeto da classe
               Labirinto que representa o labirinto do jogo;
               Cada posição do labirinto contém um dos caracteres
               em CARACTERES_LABIRINTO (= '+. ').
    '''         
    #--------------------------------------------------------------
    def __init__(self, lin, col, lab):
        '''(Fantasma, int, int, Labirinto) -> None

        Construtor: recebe inteiros `lin`, `col` e referências/apelidos
          
            - `self`: para o objeto Fantasma que está sendo construído e
            - `lab` : para um objeto da classe Labirinto.

        O método cria e retorna um objeto que representa um fantasma.

        O fantasma criado ocupa a posição [lin][col] do labirinto.

        Inicialmente a sua direção deve ser sorteada dentre as direções 
        possíveis.

        Atenção: self.lab deve ser um apelido do parâmetro lab e 
            __não__ um clone.

        O método pode supor que sempre há uma direção possível para o
        fantasma.
        
        Sugestões:
            - para obter as direções possíveis use o método direcoes_possiveis()
              do objeto lab (classe Labirinto)
            - para o sorteio use random.choice(lista) que retorna
              um item sorteado da lista:

        >>> sorteado = random.choice(['a',2,True])
        >>> print(sorteado)
        True
        >>> sorteado = random.choice(['a',2,True])
        >>> print(sorteado)
        'a'
        >>> sorteado = random.choice(['a',2,True])
        >>> print(sorteado)
        'a'
        >>> sorteado = random.choice(['a',2,True])
        >>> print(sorteado)
        2
        >>> sorteado = random.choice(['a',2,True])
        >>> print(sorteado)
        'a'
        >>> 

        Método mágico/especial: usado pelo Python quando criamos
            escrevemos Pacman(). Não tem `return`.
        '''
        #print("Vixe! Ainda não fiz o método Fantasma.__init__() :-(")
        self.lin = lin
        self.col = col
        self.labirinto = lab        
        direcao = random.choice(self.labirinto.direcoes_possiveis(lin,col))
        self.dir = direcao
        print("Fantasma.__init__(): criado Fantasma: posição [%d][%d], direção '%s'"%(lin,col,direcao))
              
    #--------------------------------------------------------------        
    def __str__(self):
        '''(Fantasma) -> str

        Recebe um Fantasma referenciada por `self` e constrói e retorna 
        o string utilizado por print() para imprimir informações sobre
        o fantasma. 

        Esse também é o string retornado pela função nativa str().
        '''        
        
        string = "Fantasma: posição [%d][%d], direcao '%s'"%(self.lin,self.col,self.dir)       
        
        return string

    
    #--------------------------------------------------------------
    def posicao(self):
        '''(Fantasma) -> int, int

        Recebe um Fantasma referenciado por `self` e retorna dois inteiros 
        lin e col tais que o fantasma está na posição [lin][col].
        '''
        lin = self.lin
        col = self.col
        
        return lin,col

    
    #--------------------------------------------------------------
    def direcao(self):
        '''(Fantasma) -> str

        Recebe um Fantasma referenciado por `self` e retorna um símbolo
        em 'wasd' representando a direção do último movimento do fantasma.
        '''
        string = ''
        string = string + self.dir
        return string


        
    #--------------------------------------------------------------
    def mova(self):
        '''(Fantasma) -> None

        Recebe um Fantasma referenciado por `self` e move o fantasma 
        de acordo com as regras do EP2.

        O método pode supor que sempre há uma direção possível para o
        fantasma.

        Sugestão: inspire-se na sua função movimentaFantasmas() do EP2.
        '''
        '''PODE SORTEAR DIREÇAO OPOSTA DA DE ANTES?? SE SIM, TA FUNCIONANDO'''        
        #print("Vixe! Ainda não fiz o método Fantasma.mova() :-(")   
        direcao = self.dir
        andou = False
        labirinto = self.labirinto
        lin_anterior = self.lin
        col_anterior = self.col
        matriz_labirinto = labirinto.lab
        
        #Se for pra CIMA
        if direcao == 'w':
            lin = extras.cic(self.lin - 1, len(matriz_labirinto))
            col = extras.cic(self.col, len(matriz_labirinto[1]))
            self.lin = lin
            self.col = col
            andou = True

       #Se for pra DIREITA
        if direcao == 'd':
            lin = extras.cic(self.lin, len(matriz_labirinto))
            col = extras.cic(self.col + 1, len(matriz_labirinto[1]))
            self.lin = lin
            self.col = col
            andou = True

       #Se for pra BAIXO       
        if direcao == 's':
            lin = extras.cic(self.lin + 1, len(matriz_labirinto))
            col = extras.cic(self.col, len(matriz_labirinto[1]))
            self.lin = lin
            self.col = col
            andou = True

        #Se for pra ESQUERDA
        if direcao == 'a':
            lin = extras.cic(self.lin, len(matriz_labirinto))
            col = extras.cic(self.col - 1, len(matriz_labirinto[1])) 
            self.lin = lin
            self.col = col
            andou = True
            
        if andou == True:
            print("Fantasma.mova(): fantasma moveu-se de [%d][%d] para [%d][%d]"%(lin_anterior,col_anterior,self.lin,self.col))
            lista_dir_possiveis =  self.labirinto.direcoes_possiveis(lin,col)
            if direcao == 'w':
                lista_dir_possiveis.remove('s')
            if direcao == 'd':
                lista_dir_possiveis.remove('a')
            if direcao == 's':
                lista_dir_possiveis.remove('w')
            if direcao == 'a':
                lista_dir_possiveis.remove('d')
            direcao = random.choice(lista_dir_possiveis)
            self.dir = direcao

            