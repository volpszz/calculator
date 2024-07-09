# operações basicas

import math

def adicao (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def multiplicacao (a,b):
    return a * b

def divisao (a,b):
    if b == 0:
        return "Não é possivel fazer divisão por zero."
    return a / b

def potencia (a,b):
    return a ** b

def raiz (a):
    return math.sqrt(a)
    
       
 
    

print("Escolha qual operação:")
print("1.adiçao")
print("2.subtração")
print("3.multiplicação")
print("4.divisão")
print("5.potencia")    
print("6.raiz quadrada")   

while True:


    escolha = input("Escolha a opção (1/2/3/4/5/6:) ")
    if escolha in ( "1", "2", "3", "4","5",):        
        a = float(input("Digite o primeiro numero: "))    
        b = float(input("Digite o segundo numero: "))



    if escolha in ("6"):
        ab = float(input("Digite o número da raiz: "))

    

    


    if escolha == '1':
   
            print(adicao(a,b))

    elif escolha == '2':
   
             print(subtracao(a,b)) 
              
    elif escolha == '3':
   
             print(multiplicacao(a,b))

    elif escolha == '4':
   
             print(divisao(a,b))

    elif escolha == '5':
            print(potencia(a,b)) 

    elif escolha == '6':
             print(f"√{ab} = {raiz(ab)}")




    else:
         print("Opção inválida, Digite um número de 1 a 6.")
         continue        

    nova_operação = input("Deseja fazer uma nova operação? (S/N): ")
    if nova_operação.lower() != 's':
        break




    print("programa encerrado.")
    

        

            