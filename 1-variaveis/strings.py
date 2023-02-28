# ASSIM COMO NUMEROS, STRINGS SÃO SOMAVEIS
string1 = "Ola"
string2 = "Mundo"
string3 = string1 + " " + string2 # "Ola Mundo"

#Outra maneira interessando para isso usando .format
stringFormat = "valor1 = {}, valor2 = {}".format("vou entrar dentro das chaves 1",2)
print(stringFormat) # valor1 = vou entrar dentro das chaves 1, valor2 = 2

#Mais uma forma
outra = f"valor1 = {string1}, valor2 = {string2}"
print(outra) # valor1 = Ola, valor2 = Mundo

# NÃO É OBRIGATORIO CRIAR PARA USAR
print(string1+" "+string2)
print(f"{string1} {string2}")
print("{} {}".format(string1,string2))

# PODEMOS DIVIDIR STRINGS COM SPLIT STRING.DIVIDIR("NESSE lUGAR")
stringParaSerDividida = "Eu sou uma string"
dividido = stringParaSerDividida.split("sou") # DIVIDIMOS
# ISSO IRA GERAR UMA ARRAY COM OS ITENS ["Eu","uma string"]
print(dividido[1]) #vai printar "uma string" pois é a mesma coisa que ["Eu","uma string"][1]