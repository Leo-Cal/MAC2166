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
import sys # sys.exit()

# as constantes que podem ser usadas estão em constantes.py
# para usá-las não é necessário escrever "constantes."
from constantes import *  # PACDOT, VAZIO, PACMAN, CARACTERES_VALIDOS ...

# descomente a linha a seguir se você usa alguma função do módulo extras
# import extras

#----------------------------------------------------------------
class Labirinto:
    '''Classe utilizada para representar um labirinto.

    O labirinto é representado através de uma matriz (= lista de listas). 

    Cada objeto dessa classe tem dois atributos de estado:

        * `lab`: é uma matriz (lista de listas) que representa o labirinto.
           Cada posição da matriz pode conter um caractere dos caracteres
           que estão no string CARACTERES_VALIDOS (= '+CF. ', 
           veja o arquivo constantes.py).

        * `pacdots`: é um inteiro que indica o número de pacdots no 
           labirinto.  
 
    Você deverá escrever os métodos sugeridos a seguir.

    '''                              

    #------------------------------------------------------------
    # Não modifique o método a seguir.
    def __init__(self, nome_arquivo):
        '''(Labirinto,str) -> None

        Construtor: recebe uma referência 

            - `self` para o objeto Labirinto que está sendo construído

        e um string `nome_arquivo` com o nome de um arquivo que contém 
        um labirinto. 

        O método examina o arquivo `nome_arquivo` e cria e retorna um 
        objeto da classe Labirinto.
 
        Cada posição do labirinto contém um dos caracteres em
        CARACTERES_VALIDOS (ver constantes.py).

        Se algum problema for detectado uma mensagem deve ser exibida e a 
        execução do programa será interrompida (sys.exit(0)).
        
        Método mágico: retorna, mas não tem `return`.
        '''
        # apelidos para a matriz do labirinto e para o número de pacdots
        lab     = []
        pacdots = 0
        
        # abra o arquivo. 
        try:
            arquivo = open(nome_arquivo, 'r')
        except:
            print("Labirinto.__init__(): ERRO: não consegui abrir o arquivo '%s'" %nome_arquivo)
            sys.exit(0)

        # leia todas as linhas do arquivo
        linhas_arq = arquivo.readlines()
        n = len(linhas_arq) # número de linhas no arquivo

        # feche o arquivo
        arquivo.close()

        # remova os caracteres brancos no final de cada linha
        i = 0
        while i < n and linhas_arq[i] != '':
            linhas_arq[i] = linhas_arq[i].rstrip() 
            i += 1

        # se o labirinto é vazio, imprima mensagem de erro e encerre a execução
        if i == 0:
            print('Labirinto.__init__(): ERRO: labirinto não pode ser vazio')
            sys.exit(0)
            
        # dimensão do labirinto será n_lin x n_col
        n_lin = i # linhas após a primeira em branco serão ignoradas
        n_col = len(linhas_arq[0])
        
        # crie a matriz com o labirinto 
        encontrou_pacman = False
        i = 0
        while i < n_lin:
            # construa a linha i do labirinto
            linha_lab = []
            
            # se as linhas não tem o mesmo tamanho, encerre a execução
            if len(linhas_arq[i]) != n_col:
                print('Labirinto.__init__(): ERRO: linhas devem ter o mesmo tamanho (linha=%d)' %i)
                sys.exit(0)

            j = 0
            while j < n_col:
                # coloque caractere na linha do labirinto (=lista)
                linha_lab.append(linhas_arq[i][j])
                
                # se as linhas tem algum caractere inválido, encerre a execução
                if linhas_arq[i][j] not in CARACTERES_VALIDOS:
                    print("Labirinto.__init__(): ERRO: caractere inválido ('%s') encontrado"
                                 %linhas_arq[i][j])
                    sys.exit(0)
                
                # encontrou um Pac-Man
                if linhas_arq[i][j] == PACMAN:
                    # se já havia encontrado um Pac-Man, encerre a execução
                    if encontrou_pacman:
                        print('Labirinto.__init__(): ERRO: Pac-Man já foi especificado ([%d][%d])' %(i,j))
                        sys.exit(0)
                    encontrou_pacman = True
                elif linhas_arq[i][j] == PACDOT:
                    pacdots += 1
                    
                # vá para o próximo caractere em linhas_arq[i]         
                j += 1

            # coloque linha no labirinto    
            lab.append(linha_lab)

            # vá para a próxima linha
            i += 1

        # se um pacman nao foi encontrado, encerre a execução
        if not encontrou_pacman:
            print('Labirinto.__init__(): ERRO: Pac-Man não foi encontrado no labirinto')
            sys.exit(0)

        # crie os atributos de estado do objeto Labirinto   
        self.lab     = lab
        self.pacdots = pacdots

    #-----------------------------------------------------------------
    def __str__(self):
        '''(Labirinto) -> str

        Recebe um Labirinto referenciado por `self` e cria e 
        retorna um string que poderá ser exibido por print() para
        imprimir um Labirinto.

        Esse também é o string retornado pela função nativa str().

        Para produzir o efeito de uma mudança de linha, coloque 
        no string um '\n'.

        Sugestão: inspire-se na função imprimeLabirinto() do EP2.
            Você deve trocar os prints pela criação de um string.
            Aqui será muito mais simples, pois você não precisa 
            se preocupar com o conteúdo de cada posição.
        '''
        #return "Vixe! Ainda não fiz o método Labirinto.__str__() :-("
        labirinto = self.lab
        string = ""        
        for i in range (len(labirinto)):
            if i > 0:
                string = string + "\n"
            for j in range (len(labirinto[1])):
                string = string + labirinto[i][j]
                string = string + " "
        
        return string                
                
                
            
        
    #-----------------------------------------------------------------
    def dimensao(self):
        '''(Labirinto) -> int, int

        Recebe um Labirinto referenciado por `self` e retorna o 
        número de linhas e colunas do labirinto.
        '''
        #print("Vixe! Ainda não fiz o método Labirinto.dimensao() :-(")
        n_lin = len(self.lab)
        n_col = len(self.lab[1])
        return n_lin, n_col
        

    #-----------------------------------------------------------------
    def get(self, lin, col):
        '''(Labirinto, int, int) -> str

        Recebe um Labirinto referenciado por `self` e inteiros 
        `lin` e `col` e retorna o caractere que está na posição
        [lin][col] do labirinto 
        '''
        #print("Vixe! Ainda não fiz o método Labirinto.get() :-(")
        labirinto = self.lab
        i = lin
        j = col
        caractere = ""
        caractere = caractere + labirinto[i][j]
        return caractere
        
        

    #-----------------------------------------------------------------
    def put(self, lin, col, valor):
        '''(Labirinto, int, int, objeto) -> None

        Recebe um Labirinto referenciado por `self`, inteiros 
        `lin` e `col` e um  objeto `valor` e coloca `valor` na 
        na posição [lin][col] do labirinto.

        Este método deve atualizar o atributo `pacdots`. 
        '''
        #print("Vixe! Ainda não fiz o método Labirinto.put() :-(")
        labirinto = self.lab
        i = lin
        j = col
        labirinto[i][j] = valor
        if valor == PACDOT :
            self.pacdots = self.pacdots + 1
            

    #-----------------------------------------------------------------        
    def no_pacdots(self):
        '''(labirinto) -> int

        Recebe um Labirinto referenciado por `self` e retorna o número de
        pacdots no labirinto.
        '''
        #print("Vixe! Ainda não fiz o método Labirinto.no_pacdots() :-(")
        n_pacdot = 0
        labirinto = self.lab
        for i in range (len(labirinto)):
            for j in range (len(labirinto[1])):
                if labirinto[i][j] == PACDOT:
                    n_pacdot = n_pacdot + 1
        
        return n_pacdot            
        
    #-----------------------------------------------------------------
    def direcoes_possiveis(self,lin,col):
        '''(Labirinto, int, int) -> list

        Recebe um Labirinto referenciado por `self` e inteiros
        `lin` e `col` representando a posição [lin][col] do labirinto.

        O método cria e retorna uma lista com caracteres no string DIRECOES 
        que representam as direções possíveis para as quais um Pac-Man ou 
        Fantasma poderia se movimentar se estivesse na posição [lin][col].
        '''
        #print("Vixe! Ainda não fiz o método Labirinto.direcoes_possiveis() :-(")
        direções = []
        labirinto = self.lab
        i1 = lin + 1   
        i2 = lin - 1
        j1= col + 1
        j2 = col - 1
        
        if i1 < 0 :
            i1 = len(labirinto) + i1
        if i1 >= len(labirinto):
            i1 = i1 - len(labirinto)
            
        if i2 < 0 :
            i2 = len(labirinto) + i2
        if i2 >= len(labirinto):
            i2 = i2 - len(labirinto)
        
        if j1 < 0 :
            j1 = len(labirinto[1]) + j1
        if j1 >= len(labirinto[1]):
            j1 = j1 - len(labirinto[1])
       
        if j2 < 0 :
            j2 = len(labirinto[1]) + j2
        if j2 >= len(labirinto[1]):
            j2 = j2 - len(labirinto[1])
            
        if labirinto[i2][col] != PAREDE :
            direções.append('w')
        if labirinto[lin][j2] != PAREDE :
            direções.append('a')
        if labirinto[i1][col] != PAREDE :
            direções.append('s')
        if labirinto[lin][j1] != PAREDE:
            direções.append('d')
        
        return direções
            

    #-----------------------------------------------------------------
    def matriz(self):
        '''(Labirinto) -> matriz (list of list)

        Recebe um Labirinto referenciado por `self` e cria e retorna 
        um clone/cópia da matriz self.lab.
        '''
        #print("Vixe! Ainda não fiz o método Labirinto.matriz() :-(")
        matriz = []
        labirinto = self.lab
        for i in range (len(labirinto)):
            linha =[]
            for j in range  (len(labirinto[1])):
                linha.append(labirinto[i][j])
            matriz.append(linha)    
                
        return matriz


 
