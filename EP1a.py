def main():
  print("==========================\nBem vindo ao Jogo do Bixo!!\n==========================")   
  din =0.00
  float(din)
  vap = float(input("Digite o valor da aposta [1-1000]: "))
  while 1<=vap<=1000: 
      nap = float(input("Digite número apostado: "))
      nso = float(input("Digite número sorteado: "))  
      if nap == nso:
          din = din + (vap * 2)
          vap = vap*2
          print("Parabéns,você ganhou %.2f"%vap,"reais!\nSaldo atual: %.2f" %din)
          print("----------------------------------------------------")
          vap = float(input("Digite o valor da aposta[1-1000]: "))  
      if nap != nso:
          din = din - vap
          print("Você perdeu %.2f"%vap,"reais!\nSaldo atual: %.2f"%din)
          print("----------------------------------------------------")
          vap = float(input("Digite o valor da aposta[1-1000]: "))      

  print("\n+++++++++++++++++++++++++++++\n")
  if din >= 0:
          print("Parabéns, você ganhou %.2f"%din,"reais.\nVolte Sempre!")
  else:
          print("Você nos deve %.2f"%din,"reais...\nVolte sempre!")
          
main()          