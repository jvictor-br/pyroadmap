# TIPOS DE VARIAVEIS
string = "string"
numero = 1 # valor inteiro
booleano = False # pode ser True ou False
tipoFloat = 0.2 # valor não inteiro

# COLEÇOES DE ITENS

# DICIONARIO
dicionario = {"chave1":"valor1","segunda chave":2} # perceba que os itens definidos são {nomeDoItem:valorDesseItem} e usado a virgula para adicionar mais de 1
paraAcessarItemDoDicionario = dicionario["chave1"] # retorna "valor1", lembrando que o dicionario é {nomeDoItem:valorDesseItem}, "chave1" é o nome do Item dentro do dicionario, "valor" é o valor do item

# LISTA
lista = ["string",4678,"<- numero", True,False,"<- booleano",["eu sou a outra lista","dentro da lista"],{"dicionario":"dentro da lista"}] # lista ou array, contem varios itens,que podem ser de diferentes tipos
# para acessar use lista[POSICAO DO ITEM QUE COMEÇA DO 0], ou seja
lista[0] #É IGUAL A "string"
lista[1] #É igual a 4678
lista[6] #É igual a lista ["eu sou a outra lista","dentro da lista"]
lista[6][1] #É igual a mesca coisa que ["eu sou a outra lista","dentro da lista"][1] ou seja, "dentro da lista"