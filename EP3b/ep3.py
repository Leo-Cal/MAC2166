"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESSE 
  PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO. 
  ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA 
  SERÃO TRATADOS SEGUNDO OS CRITÉRIOS DIVULGADOS NA PÁGINA DA 
  DISCIPLINA. ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS 
  E, AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

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
import random # para random.seed()

# as constantes que podem ser usadas estão em constantes.py
# para usá-las não é necessário escrever "constantes."
from constantes import * 

# módulo com a definição da classe Labirinto
# os métodos da classe Labirinto poderão ser usados:
#    dimensao(), get(), put(), direcoes_possiveis(), matriz(), ... 
from labirinto import *

# módulo com a definição da classe Pacman
# os métodos da classe Pacman poderão ser usados:
#    posicao(), direcao(), morra(), reposicione(),... 
from pacman import *

# módulo com a definição da classe Fantasma
# os métodos da classe Fantasma poderão ser usados:
#    posicao(), direcao(), mova(), ... 
from fantasma import *

# módulo com a definição da classe Console
# os métodos da classe Console poderão ser usados:
#    no caso, o métodos __str__() quando usamos print()
from console import *

# CONSTANTES
PROMPT = "Direção (w:cima, a:esquerda, s:baixo, d:direita, x:sair): "

# caractere que se digitado encerra a execução do programa
SAIR   = 'x'

#----------------------------------------------------------------------
#
#   M A I N 
#
#----------------------------------------------------------------------

#----------------------------------------------------------------------
def main():
    # NÃO MODIFIQUE AS LINHAS ABAIXO
    # ------------------------------
    semente = 0
    random.seed(semente)

    print("Bem-vindo ao bom e velho Come-come!")
    nome_do_arquivo = input("Digite o nome do arquivo do labirinto ou enter para o labirinto padrão: ")
    if nome_do_arquivo == '':
        nome_do_arquivo = "labirinto-original.txt"

    # leitura da configuração inicial do labirinto
    lab = Labirinto(nome_do_arquivo)
    
    

    # AGORA VOCÊ PODE MODIFICAR O MAIN
    
    labirinto = Labirinto(nome_do_arquivo)
    labirinto_visual = Labirinto(nome_do_arquivo)
    
    pacman = crie_pacman(labirinto)    
    fantasmas = crie_fantasmas(labirinto)
    print(labirinto)
    console = Console(pacman,fantasmas,labirinto)
    pontos = pacman.pontos()
    
    n_pacdots = labirinto.no_pacdots()
    n_mortes = 0
    
    
    
    print(console)
   
    while pacman.no_vidas() > 0 and labirinto.no_pacdots() > 0 :
    
    #MOVIMENTAR FANTASMAS
        
        for i in range (len(fantasmas)):

            lin_a_f,col_a_f = fantasmas[i].posicao()

            fantasmas[i].mova()
            
            lin_d_f, col_d_f = fantasmas[i].posicao()
                            
            console.lab.lab[lin_a_f][col_a_f] = labirinto.lab[lin_a_f][col_a_f]
            
        
 #---------------------------------------------------------------------       
  #VERIFICAR COLISAO ANTES DE MOVIMENTAR PACMAN
        if houve_colisao(pacman,fantasmas):
            cópia = labirinto.matriz()          
            pacman.morra()
            n_mortes = n_mortes + 1

            labirinto.lab[lin_d_p][col_d_p] = COLISAO
            print(labirinto)
            labirinto.lab[lin_d_p][col_d_p]= cópia[lin_d_p][col_d_p]
            
       #IMPLICAÕES DA COLISAO

        if houve_colisao(pacman,fantasmas):
            print("Você perdeu sua %dª vida..."%n_mortes)
            if n_mortes < 3 :            
              lin_r = int(input("Digite a linha onde quer recomeçar: "))
              col_r = int(input("Digite a coluna onde quer recomeçar: "))
              lin_r = extras.cic(lin_r,len(labirinto.lab))
              col_r = extras.cic(col_r,len(labirinto.lab[1]))
              print()
              print(labirinto)
              print()
              
              ##VERIFICAR SE TEM FANTASMA NA POSIÇÃO
              pode = True                
              for i in range (len(fantasmas)):
                  fl,cl = fantasmas[i].posicao()
                  if lin_r == fl and col_r == cl:
                      pode = False    
             
              while (console.lab.lab[lin_r][col_r] != VAZIO) or (pode == False):
                 print("Posição inválida. Digite uma nova posição, que tenha VAZIO.")
                 lin_r = int(input("Digite a linha onde quer recomeçar: "))
                 col_r = int(input("Digite a coluna onde quer recomeçar: "))
                 lin_r = extras.cic(lin_r,len(labirinto.lab))
                 col_r = extras.cic(col_r,len(labirinto.lab[1]))
                 
                 pode = True
                 for i in range (len(fantasmas)):
                  fl,cl = fantasmas[i].posicao()
                  if lin_r == fl and col_r == cl:
                      pode = False    
              
              print("main(): pacman mudou-se de [%d][%d] para [%d][%d]"%(lin_d_p,col_d_p,lin_r,col_r))
              pacman.reposicione(lin_r, col_r)
              print(console)
        
        pontos = pacman.pts
        if n_mortes == 3:
            print("Terminou o jogo... Você conseguiu %d pontos"%pontos)
        if console.lab.no_pacdots() == 0:
            print("Você venceu!!!  Terminou o jogo com %d pontos e %d vidas!"%(pontos,pacman.vidas))

#----------------------------------------------------------------------            
       #Só continua o programa se ainda tiver vida
       
        if pacman.no_vidas() > 0 and labirinto.no_pacdots() > 0 :
  
  #MOVIMENTAR PACMAN
  #------------------------------------------------------
            lin_a_p, col_a_p = pacman.posicao()
            labirinto.lab[lin_a_p][col_a_p] = VAZIO
            direcao = input("Direção de movimento do pacman: ")

            pacman.mova(direcao)
    
            lin_d_p, col_d_p = pacman.posicao()
        
        
            labirinto.lab[lin_d_p][col_d_p] = VAZIO
        
  #----------------------------------------------------------      
    
                            
                
            
 #--------------------------------------------------------------------
   #VERIFICAR COLISAO E IMPRIMIR LAB
            if houve_colisao(pacman,fantasmas):
                cópia = labirinto.matriz()          
                pacman.morra()
                n_mortes = n_mortes + 1

                labirinto.lab[lin_d_p][col_d_p] = COLISAO
                print(labirinto)
                labirinto.lab[lin_d_p][col_d_p]= cópia[lin_d_p][col_d_p]

            else:
                console.lab.lab[lin_d_p][col_d_p] = labirinto.lab[lin_d_p][col_d_p]  
                print(console)
#------------------------------------------------------------------------------- 
          
          #IMPLICAÕES DA COLISAO
            if houve_colisao(pacman,fantasmas):
              print("Você perdeu sua %dª vida..."%n_mortes)
              if n_mortes < 3 :            
                  lin_r = int(input("Digite a linha onde quer recomeçar: "))
                  col_r = int(input("Digite a coluna onde quer recomeçar: "))
                  lin_r = extras.cic(lin_r,len(labirinto.lab))
                  col_r = extras.cic(col_r,len(labirinto.lab[1]))
                  print()
                  print(labirinto)
                  print()
                 #VERIFICAR SE TEM FANTASMA NA POSIÇÃO
                  
                  pode = True                    
                  for i in range (len(fantasmas)):
                      fl,cl = fantasmas[i].posicao()
                      if lin_r == fl and col_r == cl:
                          pode = False    
                  
                  while console.lab.lab[lin_r][col_r] != VAZIO or not pode :
                      print("Posição inválida. Digite uma nova posição, que tenha VAZIO.")
                      lin_r = int(input("Digite a linha onde quer recomeçar: "))
                      col_r = int(input("Digite a coluna onde quer recomeçar: "))
                      lin_r = extras.cic(lin_r,len(labirinto.lab))
                      col_r = extras.cic(col_r,len(labirinto.lab[1]))
                      
                      pode = True                        
                      for i in range (len(fantasmas)):
                          fl,cl = fantasmas[i].posicao()
                          if lin_r == fl and col_r == cl:
                              pode = False    
                  print("main(): pacman mudou-se de [%d][%d] para [%d][%d]"%(lin_d_p,col_d_p,lin_r,col_r))
                  pacman.reposicione(lin_r, col_r)
                  print(console)
        
            pontos = pacman.pts
            
            if n_mortes == 3:
                print("Terminou o jogo... Você conseguiu %d pontos"%pontos)
            if console.lab.no_pacdots() == 0:
                print("Você venceu!!!  Terminou o jogo com %d pontos e %d vidas!"%(pontos,pacman.vidas))
  #------------------------------------------------------------------------------------          
        
        
        
#----------------------------------------------------------------------
def crie_pacman(lab):
    '''(Labirinto) -> Pacman

    Recebe uma referência `lab` a um objeto da classe Labirinto.

    Percorre o labirinto em busca de um caractere PACMAN definido 
    no módulo constantes.py. Ao encontrar o caractere, a função o 
    substitui por VAZIO no labirinto, e cria e retorna um objeto 
    da classe Pacman que representa o Pac-Man.

    O objeto Labirinto __deve__ ser acessado apenas através dos métodos
    da sua classe, conforme a sua definição no módulo labirinto.py.

    Para criar um objeto Pacman veja a definição da sua classe no 
    módulo pacman.py.
    '''
    #print("Vixe! Ainda não fiz a função crie_pacman() :-(") 
    labirinto = lab.lab
    for i in range (len(labirinto)):
        
        for j in range (len(labirinto[1])):

            if labirinto[i][j] == PACMAN:

                labirinto[i][j] = VAZIO
                print("crie_pacman(): Pac-Man encontrado na posição [%d][%d]"%(i,j))
                pacman = Pacman(i,j,lab)
    return pacman            
#----------------------------------------------------------------------
def crie_fantasmas(lab):
    '''(Labirinto) -> lista de Fantasma

    Recebe uma referência `lab` a um objeto da classe Labirinto.

    Percorre o labirinto em busca de caracteres FANTASMA definidos no 
    módulo constantes.py. Ao encontrar um destes caracteres, a função 
    o substitui por um PACDOT no labirinto, cria um objeto da classe 
    Fantasma que representa esse fantasma e o acrescenta à lista que 
    será retornada pela função. 

    O objeto Labirinto __deve__ ser acessado apenas através dos métodos
    da sua classe, conforme a sua definição no módulo labirinto.py.

    Para criar um objeto Fantasma veja a definição da sua classe no 
    módulo fantasma.py.
    '''
    #print("Vixe! Ainda não fiz a função crie_fantasma() :-(") 
    labirinto = lab.lab
    listafantasma = []    
    for i in range (len(labirinto)):
        for j in range (len(labirinto[1])):
            if labirinto[i][j] == FANTASMA:
                labirinto[i][j] = PACDOT
                fant = Fantasma(i,j,lab)
                listafantasma.append(fant)
    return listafantasma            
            
    
#----------------------------------------------------------------------
def houve_colisao(pac_man, fantasmas):
    '''(Pacman, lista de Fantasma) -> bool

    Recebe uma referência `pac_man` a um objeto da classe Pacman e
    uma lista `fantasmas` de referências a objetos da classe Fantasma.
    A função verifica se algum fantasma ocupa a mesma posição do Pac-Man,
    em caso afirmativo retorna True, do contrário retorna False. 
    '''
    #print("Vixe! Ainda não fiz a função houve_colisao() :-(")
    linp = pac_man.lin
    colp = pac_man.col
    for i in range (len(fantasmas)):
        fantasma = fantasmas[i]
        linf = fantasma.lin        
        colf = fantasma.col        
        if (linp == linf) and (colp == colf):
            
            return True
    
    return False        
#-----------------------------------------------------------------
# Início do espaço reservado para eventuais funções auxiliares
# usadas neste módulo
#



# fim do espaço reservado para eventuais funções auxiliares
# usadas neste módulo
#-----------------------------------------------------------------

# chamada da função main() deve ser a última linha do módulo    
main()
