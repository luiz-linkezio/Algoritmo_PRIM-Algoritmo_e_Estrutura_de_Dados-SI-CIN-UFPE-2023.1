import pandas
import sys
from collections import OrderedDict
from GeneAssociations import GeneAssociations
from PrimAlgorithm import PrimAlgorithm

original_stdout = sys.stdout

gene_associations = GeneAssociations()
prim = PrimAlgorithm()

#Turn CSV into DataFrame
infection_db = pandas.read_csv('database.csv')

#Create graph
gene_associations.add_gene_associations(infection_db)
infection_graph = gene_associations.graph

#Prim Algorithm
prim_MST, time_to_find_cure, deaths = prim.MST_creation(infection_graph) #Prim Algorithm: MST creation and the time calculation for find a cure


def ordenar_dicionario_por_chaves(dicionario):
    chaves_ordenadas = sorted(dicionario.keys())
    dicionario_ordenado = OrderedDict()
    
    for chave in chaves_ordenadas:
        dicionario_ordenado[chave] = dicionario[chave]
    
    return dicionario_ordenado

prim_MST = ordenar_dicionario_por_chaves(prim_MST)


with open('output.csv', 'w') as f:
    #Redirecionar a saída padrão para o arquivo
    sys.stdout = f

    for key, value in prim_MST.items():
        print(f"{key}", end=" ")
            
        for list in value:
            print(f"{list[0]}", end=" ")
        
        print("")

    sys.stdout = original_stdout