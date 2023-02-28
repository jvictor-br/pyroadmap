dicionario = {"chave1":"valor1","chave2":"valor2","chave3":"valor3"}

# ALTERANDO ITEM
dicionario["chave1"] = "novo valor" #{"chave1":"novo valor","chave2":"valor2","chave3":"valor3"}

# ADICIONANDO
dicionario["nova chave"] = "esse é o valor" #{"chave1":"novo valor","chave2":"valor2","chave3":"valor3","nova chave":"esse é o valor"}

# REMOVENDO
dicionario.pop("nova chave") #{"chave1":"novo valor","chave2":"valor2","chave3":"valor3"}

# RETORNA APENAS AS CHAVES
print(dicionario.keys())
# RETORNA APENAS OS VALORES
print(dicionario.values())
# RETORNA UMA LISTA DE ITENS (CHAVE,VALOR)
print(dicionario.items())
# LIMPAR DICIONARIO
dicionario.clear()