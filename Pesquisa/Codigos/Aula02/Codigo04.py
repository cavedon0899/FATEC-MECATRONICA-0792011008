
#coloca os numeros em ordem decrescente
   # numeros_sorteados.sort(reverse = True)

#Adicionar numero no final da fila
  #numeros_sorteados.append()





#Pacote para numeros aleatorios
import random
def gerarNumeros(quant_numeros, minimo, maximo):
    numeros_sorteados = []
    while len(numeros_sorteados) < quant_numeros:
        #Adicionar numero inteiro aleatorio 
        sorteio = random.randint(minimo, maximo)
        if sorteio not in numeros_sorteados:
            numeros_sorteados.append(sorteio)
            
    #coloca os numeros em ordem crescente
    numeros_sorteados.sort()
    return numeros_sorteados


numeros_mega_sena = gerarNumeros(6, 1, 60)
numeros_quina = gerarNumeros(5, 1, 80)
numeros_lotofacil = gerarNumeros(15, 1, 50)
print ('Mega:', numeros_mega_sena)
print ('Quina:', numeros_mega_sena)
print ('Lotofacil', numeros_lotofacil)

 
