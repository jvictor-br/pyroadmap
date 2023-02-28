# while é um laço, podemos pensar em "enquanto"
# enquanto (referencia <= 10):
#   faça isso

referencia = 0

while (referencia <= 5):
    print("printa isso")
    # CUIDADO AQUI, REFERENCIA SEMPRE VAI SER 0, CAUSANDO UM BUG INFINITO
    # PARA RESOLVER, ADICIONE VALOR A REFERENCIA
    referencia = referencia + 1