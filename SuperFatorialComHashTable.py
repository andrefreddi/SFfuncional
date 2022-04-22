import math
import time
import timeit
import psutil 

def superFatorial():

    chave    = 7 #input("Chave: ")
    fatorial = int(chave) 
    superFat = 1
    sfNaHashTable = hash_table.get_val(chave)

    #########################################################################
    ### Define o super fatorial da chave para a compração com a HashTable ###
    #########################################################################
    for count in range(fatorial):                  # range:  retorna uma série numérica no intervalo
          funcExpo = math.pow(count + 1, fatorial) # pow: pega dois párametro e eleva o primeiro valor pelo segundo
          superFat *= funcExpo
          fatorial -= 1 

    #########################################################################
    ### Verifica se o Super Fatorial da Chave está presente na HashTable, ###
    ### se não estiver realiza o calulo e imprime este super fatorial,    ###
    ### caso esteja presente ele imprime o super fatorial na tela         ###
    #########################################################################
    if superFat != sfNaHashTable:  #Se a chave não for igual a algum valor do hash_map, o FOR é executado
      
      hash_table.set_val(chave, superFat)
      print('Adicinado:', hash_table)

    else: #Se a chave for igual a algum valor na hash_table esse valor será printado
      print('Existia:', hash_table.get_val(chave))#hash_table.get_val(chave))

inicio = timeit.default_timer()
superFatorial()
fim = timeit.default_timer()
print ('Tempo de duracao: %f' % (fim - inicio))
print('O uso da CPU é: ', psutil.cpu_percent(4))
print('% de memória RAM usada:', psutil.virtual_memory()[2])
