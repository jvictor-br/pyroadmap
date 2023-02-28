# IF PODE SER TRADUZIDO PARA, "SE", ELSE PARA "SENÃO"
# SE (VALOR "FOR IGUAL A" TRUE):
#   FAÇA ISSO
# SENÃO:
#   FAÇA ISSO
#   <- É  IMPORTANTE USAR ESSE ESPAÇAMENTO, O NOME DISSO É IDENTAÇÃO, ENTENDE QUE "FAÇA ISSO" ESTÁ DENTRO DE "SE (VALOR "FOR IGUAL A" TRUE):"
# O MESMO CÓDIGO SÓ QUE AGORA USANDO IF ELSE
valor = True
if(valor == True):  # valor é igual a True, logo, no console aparacerá, "isso"
    print("se a condição for verdadeira, print isso")
else:
    print("senão print isso")

# QUANDO SE TEM MAIS DE UMA OPÇÃO, PODE SE USAR ELSE+IF, QUE FICA ELIF, QUE PODE SER TRADUZIDO COMO "OU ENTÃO"
valor = "sou uma string dessa vez"
if(valor == "string 2"):
    print("faça isso")
elif (valor == "sou uma string dessa vez"):
    print("ou então, se isso for verdadeira, faça isso")
else:
    print("se não, nenhuma delas foi atendido, faça isso então")

# os comparativos são
# == igual a
# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual