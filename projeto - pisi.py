import csv
import time

#==================================================
#=========== IMPORTAÇÃO DOS DADOS =================
#==================================================

lista_decrescente = []
with open("dados_descendentes.csv",'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=';') 
    for row in reader: 
        lista_decrescente.append(row)

lista_crescente = []
with open("dados_ascendentes.csv",'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=';') 
    for row in reader: 
        lista_crescente.append(row)

lista_desordenada = []
with open("dados_aleatorios.csv",'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=';')
    for row in reader:
        lista_desordenada.append(row)

#==================================================
#=========== FUNÇÕES COM OS ALGORITMOS ============
#==================================================
def funtionQuick(arr):
    def quickSort(lista):
        quickSortHelper(lista,0,len(lista)-1)

    def quickSortHelper(lista,primeiro,ultimo):
      if len(lista) == 1:
        return arr

      if primeiro < ultimo:
        divisor = partition(lista,primeiro,ultimo)
        quickSortHelper(lista,primeiro,divisor-1)
        quickSortHelper(lista,divisor+1,ultimo)

    def partition(lista,primeiro,ultimo):
      i = (primeiro-1)        
      pivo = lista[ultimo][0]    
      for j in range(primeiro, ultimo):
        if lista[j][0] <= pivo:
          i = i+1
          lista[i], lista[j] = lista[j], lista[i]
      lista[i+1], lista[ultimo] = lista[ultimo], lista[i+1]
      return (i+1)
    
    quickSort(arr)
    return arr
#----------------------------------------------------------
def funtionMerge(arr):

    def mergeSort(lista):
        if len(lista) > 1:
            meio = len(lista)//2
            lista_esq = lista[:meio]
            lista_dir = lista[meio:]
            mergeSort(lista_esq)
            mergeSort(lista_dir)

            i = j = k = 0
            
            while i < len(lista_esq) and j < len(lista_dir):
                if lista_esq[i][0] < lista_dir[j][0]:
                    lista[k]=lista_esq[i]
                    i +=1
                else:
                    lista[k]=lista_dir[j]
                    j +=1
                k +=1

            while i < len(lista_esq):
                lista[k]=lista_esq[i]
                i +=1
                k +=1

            while j < len(lista_dir):
                lista[k]=lista_dir[j]
                j +=1
                k +=1

    mergeSort(arr)
    return arr

#------------------------------------------------------

def funtionHeap(arr):
    def Maxheapify(arr, tamanho, i): 
        maior = i  #inicia com i como o maior
        l = 2 * i + 1     #left = 2*i + 1 
        r = 2 * i + 2     #right = 2*i + 2 
     
        if l < tamanho and arr[l][0] > arr[i][0]: 
            maior = l 
        else:
            maior = i
      
        if r < tamanho and arr[r][0] > arr[maior][0]: 
            maior = r 
      
        if maior != i: 
            arr[i],arr[maior] = arr[maior],arr[i]  
            Maxheapify(arr, tamanho, maior) 
  
    def heapSort(arr): 
        #esse 'for' faz o build-max-heap. 
        for i in range(len(arr), -1, -1): 
            Maxheapify(arr, len(arr), i) 
      
        for i in range(len(arr)-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i]   
            Maxheapify(arr, i, 0)

    heapSort(arr)
    return arr
#---------------------------------------------------


print('='*50)
print('CUSTO EM TEMPO: ALGORITMO X LISTA'.ljust(50))
print('='*50)

print('-'*50)
print('Merge Sort')
print('-'*50)

ini = time.time()
print(funtionMerge(lista_crescente))
fim = time.time()
print("Função Merge com lista crescente: ", fim-ini)

ini = time.time()
print(funtionMerge(lista_decrescente))
fim = time.time()
print("Função Merge com lista decrescente: ", fim-ini)

ini = time.time()
print(funtionMerge(lista_desordenada))
fim = time.time()
print("Função Merge com lista desclassificada: ", fim-ini)

print('-'*50)
print('Quick Sort')
print('-'*50)

ini = time.time()
print(funtionQuick(lista_crescente))
fim = time.time()
print("Função Quick com lista crescente: ", fim-ini)

ini = time.time()
print(funtionQuick(lista_decrescente))
fim = time.time()
print("Função Quick com lista decrescente: ", fim-ini)

ini = time.time()
print(funtionQuick(lista_desordenada))
fim = time.time()
print("Função Quick com lista desclassificada: ", fim-ini)

print('-'*50)
print('Heap Sort')
print('-'*50)

ini = time.time()
print(funtionHeap(lista_crescente))
fim = time.time()
print("Função Heap com lista crescente: ", fim-ini)

ini = time.time()
print(funtionHeap(lista_decrescente))
fim = time.time()
print("Função Heap com lista decrescente: ", fim-ini)

ini = time.time()
print(funtionHeap(lista_desordenada))
fim = time.time()
print("Função Heap com lista desclassificada: ", fim-ini)
