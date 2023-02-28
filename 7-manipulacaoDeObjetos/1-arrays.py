array = ["item0","item1","item2"]
array2 = ["itemDaLista2","segundoitemDaLista2"]

#adicionar item com APPEND
array.append("novo item") # ["item0","item1","item2", "novo item"]

# JUNCAO DE LISTAS
# COM APPEND ADICIONA O ITEM ARRAY2 AO ARRAY
array.append(array2) # ['item0', 'item1', 'item2', 'novo item', ['itemDaLista2', 'segundoitemDaLista2']]

# COM EXTEND ADICIONA OS ITENS DO ARRAY2 NO ARRAY
array.extend(array2) # ['item0', 'item1', 'item2', 'novo item', 'itemDaLista2', 'segundoitemDaLista2']

# misturar itens
array.sort() #mistura posicao dos itens

# TAMANHO DA LISTA
len(array2) #vai retornar quantos itens tem no array