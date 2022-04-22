# Codigo Base para contrucao do com Hash Table (Nosso codigo teste)

import psutil 

def superfactorial(n):
  
    valor = 1
    fatorial = []
    for i in range(1, n + 1):
        valor = valor * i
        fatorial.append(valor)
 
    SuFatorial = [1]
    for i in range(1, len(fatorial)):
        SuFatorial.append((SuFatorial[-1]*fatorial[i]))
  
    return SuFatorial

n = 4  
SuFatorial = superfactorial(n)
print(SuFatorial[-1])

def alguma_funcao():
  superfactorial(6)

inicio = timeit.default_timer()
alguma_funcao()
fim = timeit.default_timer()
print ('Tempo de duracao: %f' % (fim - inicio))
print('O uso da CPU é: ', psutil.cpu_percent(4))
print('% de memória RAM usada:', psutil.virtual_memory()[2])
