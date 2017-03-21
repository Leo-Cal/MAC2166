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

# módulo onde estarão as funções a serem implementadas para fazer todo
# o controle e impressão do jogo (É o arquivo pacman.py)
import pacman
import extras

# Se você criou funções adicionais e colocou em extras.py,
# descomente a linha abaixo
#import extras

# módulo para definição da semente para sorteio dos números pseudo
# aleatórios
import random


# ======================================================================
#
#   M A I N 
#
# ======================================================================

def main():

    # !!!! NÃO MODIFIQUE AS LINHAS ABAIXO !!!! 
    semente = 0
    random.seed(semente)

    # leitura da configuração inicial do labirinto
    nomeDoArquivo = input("Digite o nome do arquivo do labirinto: ")    
    lab = pacman.leLabirinto(nomeDoArquivo)

    # !!!! AGORA VOCÊ PODE MODIFICAR O MAIN !!!! 
###CONSTANTES    
    ESQUERDA = 0   # 'a'
    DIREITA  = 1   # 's'
    CIMA     = 2   # 'w'
    BAIXO    = 3   # 'z'
    PARADO   = 4

    cont = 1 ##usada para movimentar fantasmas
    
    
##CRIAÇÃO INICIAL LABIRINTO    
    listapacman = pacman.criaPacMan(lab)
    listafantasma = pacman.criaFantasmas(lab)
    pacman.imprimeLabirinto(lab,listapacman,listafantasma)  
    fim = False
    while fim == False :
##DEFINIR DIREÇÃO DE MOVIMENTO PACMAN
     direção = PARADO
     while direção != ESQUERDA and direção!= DIREITA and direção != CIMA and direção != BAIXO :
        direção = input("Direção (a - Esquerda   s - Direita   w - Cima   z - Baixo) : ")
        if direção == 'a' :
         direção = ESQUERDA
        if direção == 's' :
         direção = DIREITA
        if direção == 'w' :
         direção = CIMA
        if direção == 'z' :
         direção = BAIXO
     listapacman[2] = direção

##MOVIMENTAR FANTASMAS    
       
     if cont == 1 : ##primeira interação
         matriz_record = []
         for i in range (len(listafantasma)):
        
           
          lista_record = []
          lab[listafantasma[i][0]][listafantasma[i][1]] = '.' 
          
       ##Armazenar na lista o que tem ao redor do fantasma
          ##Direita
          linha = extras.cíclico(listafantasma[i][0], len(lab))
          coluna = extras.cíclico(listafantasma[i][1] + 1, len(lab[1]))
          lista_record.append(lab[linha][coluna])
          ##Esquerda
          linha = extras.cíclico(listafantasma[i][0], len(lab))
          coluna = extras.cíclico(listafantasma[i][1]- 1, len(lab[1]))
          lista_record.append(lab[linha][coluna])
          ##Cima
          linha = extras.cíclico(listafantasma[i][0] - 1, len(lab))
          coluna = extras.cíclico(listafantasma[i][1], len(lab[1]))
          lista_record.append(lab[linha][coluna])
          ##Baixo
          linha = extras.cíclico(listafantasma[i][0] + 1, len(lab))
          coluna = extras.cíclico(listafantasma[i][1], len(lab[1]))
          lista_record.append(lab[linha][coluna])
         
       #Armazenar lista do fantasma 'i' numa matriz
          matriz_record.append(lista_record)  
          
          
        
        
     if cont > 1 : ##depois da primeira interação
         
         for j in range(len(matriz_record)):     
        ##Colocar no lugar de cada fantasma o que tinha lá antes
          ##Se ele andou pra Direita:
          if listafantasma[j][2] == DIREITA:
              linha = extras.cíclico(listafantasma[j][0], len(lab))
              coluna = extras.cíclico(listafantasma[j][1], len(lab[1]))
              lab[linha][coluna] = matriz_record[j][0]
          ##Se ele andou pra Esquerda:
          if listafantasma[j][2] == ESQUERDA:
              linha = extras.cíclico(listafantasma[j][0], len(lab))
              coluna = extras.cíclico(listafantasma[j][1], len(lab[1]))              
              lab[linha][coluna] = matriz_record[j][1]
          ##Se ele andou pra Cima:
          if listafantasma[j][2] == CIMA:
              linha = extras.cíclico(listafantasma[j][0], len(lab))
              coluna = extras.cíclico(listafantasma[j][1], len(lab[1]))              
              lab[linha][coluna] = matriz_record[j][2]
          ##Se ele andou pra Baixo:
          if listafantasma[j][2] == BAIXO:
              linha = extras.cíclico(listafantasma[j][0], len(lab))
              coluna = extras.cíclico(listafantasma[j][1], len(lab[1]))              
              lab[linha][coluna] = matriz_record[j][3]


        ##Zerar a matriz_record e fazer denovo
         matriz_record = []
         lista_record = []
         for k in range (len(listafantasma)) : 
        ##Armazenar na lista o que tem ao redor do fantasma
          lista_record = []   
         ##Direita
          linha = extras.cíclico(listafantasma[k][0], len(lab))
          coluna = extras.cíclico(listafantasma[k][1] + 1, len(lab[1]))
          lista_record.append(lab[linha][coluna])
         ##Esquerda
          linha = extras.cíclico(listafantasma[k][0], len(lab))
          coluna = extras.cíclico(listafantasma[k][1]- 1, len(lab[1]))
          lista_record.append(lab[linha][coluna])
         ##Cima
          linha = extras.cíclico(listafantasma[k][0] - 1, len(lab))
          coluna = extras.cíclico(listafantasma[k][1], len(lab[1]))
          lista_record.append(lab[linha][coluna])
         ##Baixo
          linha = extras.cíclico(listafantasma[k][0] + 1, len(lab))
          coluna = extras.cíclico(listafantasma[k][1], len(lab[1]))
          lista_record.append(lab[linha][coluna])
         
       #Armazenar lista do fantasma 'i' numa matriz
          matriz_record.append(lista_record)
        
       ##Sortear pra todos os fantasmas novas direções, excetuando a oposta da atual         
         for l in range (len(listafantasma)):
          sorteado = False
          if listafantasma[l][2] == DIREITA and not sorteado :     
              sorteado = True            
              listafantasma[l][2] = random.randrange(0,4) 
              while listafantasma[l][2] == ESQUERDA:
                  listafantasma[l][2] = random.randrange(0,4)
          if listafantasma[l][2] == ESQUERDA and not sorteado :     
              sorteado = True            
              listafantasma[l][2] = random.randrange(0,4) 
              while listafantasma[l][2] == DIREITA:
                  listafantasma[l][2] = random.randrange(0,4)
          if listafantasma[l][2] == CIMA and not sorteado :     
              sorteado = True            
              listafantasma[l][2] = random.randrange(0,4) 
              while listafantasma[l][2] == BAIXO:
                  listafantasma[l][2] = random.randrange(0,4)
          if listafantasma[l][2] == BAIXO and not sorteado :     
              sorteado = True            
              listafantasma[l][2] = random.randrange(0,4) 
              while listafantasma[l][2] == CIMA:
                  listafantasma[l][2] = random.randrange(0,4)
              
 

            
    ##Movimentar o fantasma e aumentar 1 no contador de interação
           
     pacman.movimentaFantasmas(lab, listafantasma)
     cont = cont + 1
                   
             
           
##VERIFICAR COLISÃO E ACABAR JOGO
     if pacman.verificaColisao(listapacman,listafantasma) == True :
       pacman.imprimeLabirinto(lab, listapacman, listafantasma)
       print("Game Over! Pontos : %d"%(listapacman[3]))
       fim = True
     else:  

##MOVIMENTAR PACMAN
      
      linha_antiga_pacman = listapacman[0]
      coluna_antiga_pacman = listapacman[1]
     
     ##Ver se tem pacdot em todas as possiveis direções
      ##Direita:
      linha = extras.cíclico(listapacman[0], len(lab))
      coluna = extras.cíclico(listapacman[1] + 1, len(lab[1]))
      pacdot_direita = False    
      if lab[linha][coluna] == '.':
         pacdot_direita = True 
         
      ##Esquerda:
      linha = extras.cíclico(listapacman[0], len(lab))
      coluna = extras.cíclico(listapacman[1] - 1, len(lab[1]))
      pacdot_esquerda = False    
      if lab[linha][coluna] == '.':
         pacdot_esquerda = True     
         
      ##Cima:
      linha = extras.cíclico(listapacman[0] - 1 , len(lab))
      coluna = extras.cíclico(listapacman[1], len(lab[1]))
      pacdot_cima = False    
      if lab[linha][coluna] == '.':
         pacdot_cima = True    
         
      ##Baixo:
      linha = extras.cíclico(listapacman[0] + 1, len(lab))
      coluna = extras.cíclico(listapacman[1], len(lab[1]))
      pacdot_baixo = False    
      if lab[linha][coluna] == '.':
         pacdot_baixo = True     
      
     ##Movimentar Pacman e ver se houve colisão 
      pacman.movimentaPacMan(lab, listapacman)
      lab[linha_antiga_pacman][coluna_antiga_pacman] = ' '
      
      if pacman.verificaColisao(listapacman,listafantasma) == True :
       pacman.imprimeLabirinto(lab, listapacman, listafantasma)
       print("Game Over! Pontos : %d"%(listapacman[3]))
       fim = True
     
     ##Se não houve colisão, imprime o labirinto e verifica ganho de pacdot
      else :
       pacman.imprimeLabirinto(lab, listapacman, listafantasma)
      
      ##Ver se ganhou pacdot:
      ##Direita:
      if listapacman[2] == DIREITA and pacdot_direita :
          listapacman[3] = listapacman[3] + 1
          
      ##Esquerda:
      if listapacman[2] == ESQUERDA and pacdot_esquerda :
          listapacman[3] = listapacman[3] + 1
          
      ##Cima:
      if listapacman[2] == CIMA and pacdot_cima :
          listapacman[3] = listapacman[3] + 1
          
      ##Baixo:
      if listapacman[2] == BAIXO and pacdot_baixo :
          listapacman[3] = listapacman[3] + 1
    
     ##Verificar se ainda tem pacdots no labirinto 
      if pacman.aindaTemPacDots(lab) == False :
        print("Congratulations! Pontos : %d"%(listapacman[3]))
        fim = True
     
                
        
        
        
        


main()
