# operações basicas



def adicao (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def multiplicacao (a,b):
    if b == 0:
        return "Todo numero multiplicado por 0 é 0"
    return a * b

def divisao (a,b):
    if b == 0:
        return "Não é possivel fazer divisão por zero."
    return a / b

print("Escolha qual operação:")
print("1.adiçao")
print("2.subtração")
print("3.multiplicação")
print("4.divisão")

while True:


    escolha = input("Escolha a opção (1/2/3/4:) ")
    if escolha in ( "1", "2", "3", "4"):
        a = float(input("Digite o primeiro numero: "))    
        b = float(input("Digite o segundo numero: "))

     
        if escolha == '1':
   
            print(adicao(a,b))

        elif escolha == '2':
   
             print(subtracao(a,b)) 
              
        elif escolha == '3':
   
             print(multiplicacao(a,b))

        elif escolha == '4':
   
             print(divisao(a,b))

             break      
        
                                                          



