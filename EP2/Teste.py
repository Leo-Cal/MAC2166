import random
def main():

 lista = [1,2,3,4,5,6,7,8,9,10]
 numero = random.randrange(0,4)
 m = cíclico(10, len(lista))
 print(numero)

def cíclico(m,n):
    if m >= n:
        m = m - n
    return m
    
main()