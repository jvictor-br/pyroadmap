#(inicia a valor, condição, a cada etapa adiciona isso)
for index in range(0,10,1): # o valor da condicao começa em 0, peço para parar em 10, a cada vez que for verificado, vai executar o bloco e adicionar 1 ao valor inicial
    print("Isso vai ser executado 10x")
    print(index) # essa é a posição que está sendo executado, como se fosse aquele valor inicial, de 0, que vai sendo aumentado de 1 em 1

# for i in range(0,8,2)
    # i = 0 executa essa vez
    # i = 2 executa essa vez
    # i = 4 executa essa vez
    # i = 6 executa essa vez
    # o for vai acabar aqui, pois i+2 igual ao 8


# MELHOR USO PARA FOR
lista = ["maria","pedro","juvenal","ana"]
# para cadaitem dentro da lista
for item in lista: #vai varrer a lista
    print(item) # a referencia item, vai ser cada vez diferente
    #comecou a varrer a lista ["maria","pedro","juvenal","ana"]
    #item = "maria" dessa vez
    #item = "pedro" dessa vez
    #item = "juvenal" dessa vez
    #item = "ana" dessa vez
    #acabou os itens da lista