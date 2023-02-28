# use assim
# quando essaReferencia:
#     FOR IGUAL A "ISSO":
#       FAÇA ISSO
#     FOR IGUAL A "AQUILO":
#       FAÇA ISSO
#     SE NENHUM FOR IGUAL:
#       FAÇA ISSO
essaReferencia = "aquilo"
match essaReferencia:
    case "isso": # false, pois essaReferencia = "aquilo"
        print("isso")
    case "aquilo": # true, ou seja, vai executar esse bloco
        print('vai printar isso pois essaReferencia é igual a "aquilo"')
    case _: # _ é como se fosse um else
        print("se nenhum for igual")