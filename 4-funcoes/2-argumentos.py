print("ola mundo") # essa é uma funcao conhecida, print() está chamando uma funcao, "olá mundo" é um argumento

# DEFINIR/ CRIAR FUNCAO
# vamos criar nosso print
def meuPrint(textoQueVaiSerRecebidoQuandoForChamado):
    print(textoQueVaiSerRecebidoQuandoForChamado)

# CHAMAR
meuPrint("eu sou o texto") #textoQueVaiSerRecebidoQuandoForChamado passa a ser "eu sou o texto"

# outro exemplo
def soma(valor1,valor2):
    print(valor1+valor2)

soma(3,7) #valor1 = 3, valor2 = 7


# ARGUMENTOS OPICIONAIS
# caso chamar apenas soma() vai dar erro, pois precisamos de 2 valores, mas, tem como deixar isso opcional
def sub(valor1 = 0, valor2 = 0): # ja estamos atribuindo um valor, caso quando a funcao for chamada, não for passado nenhum valor, ela assumira o valor que passamos para ela ao definir
    print(valor1+valor2)

sub()