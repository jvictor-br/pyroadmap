# apenas vimos funcoes do tipo
def apenasPrintaAlgo(argumento):
    print(argumento)

apenasPrintaAlgo("eu sou o argumento que será printado")

# Mas uma funcao tambem pode retornar um valor com RETURN
def umaFuncaoQueRetorna():
    print("esse bloco está sendo executado")
    return "Valor retornado" # a funcao vai retornar isso

# para capturar o valor de retorno, é só atribuir essa funcao a alguma referencia

variavel = umaFuncaoQueRetorna() # variavel passará a ser "Valor retornado"

# com argumentos
def retornaSoma(arg1,arg2): # recebe 2 argumentos
    return arg1 + arg2 # retorna o valor de arg1 + arg2

somaDe3mais5 = retornaSoma(3,5)