#USAMOS ISSO PARA QUANDO TIVER ALGUM ERRO NÃO QUEBRAR O CÓDIGO
try: # tenta isso
    string = "nao sou um numero"
    subInvalida =  string - 2
    print("não vou ser printado pois string - 2 gera um erro")
except: # caso der algum erro
    print("deu erro em algo")

# para capturar o erro ao inves de except simples, usaremos except Exception as erro, printaremos o erro gerado com print(erro)
try: # tenta isso
    string = "nao sou um numero"
    subInvalida =  string - 2
    print("não vou ser printado pois string - 2 gera um erro")
except Exception as erro: # caso der algum erro
    print(erro) # printará o erro unsupported operand type(s) for -: 'str' and 'int'