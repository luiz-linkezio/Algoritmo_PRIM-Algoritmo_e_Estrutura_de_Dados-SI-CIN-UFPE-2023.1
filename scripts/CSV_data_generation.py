import pandas
import sys
from collections import OrderedDict
from scripts.GeneAssociations import GeneAssociations
from scripts.PrimAlgorithm import PrimAlgorithm


#This function generates a CSV file of the graph's connections.
def generate_CSV_data(initial_vertex=0):

    #Record of print preparation
    original_stdout = sys.stdout

    #Classes initialization
    gene_associations = GeneAssociations()
    prim = PrimAlgorithm()

    #Turn CSV into DataFrame
    infection_db = pandas.read_csv('database.csv')

    #Create graph
    gene_associations.add_gene_associations(infection_db)
    infection_graph = gene_associations.graph

    #Prim Algorithm
    prim_MST, time_to_find_cure, deaths = prim.MST_creation(infection_graph, initial_vertex) #Prim Algorithm: MST creation and the time calculation for find a cure

    #This function sorts the dictionary by its keys.
    def sort_dict_by_keys(dicionario):
        chaves_ordenadas = sorted(dicionario.keys())
        dicionario_ordenado = OrderedDict()
        
        for chave in chaves_ordenadas:
            dicionario_ordenado[chave] = dicionario[chave]
        
        return dicionario_ordenado

    #Calling the sort function to sort the dictionary
    prim_MST = sort_dict_by_keys(prim_MST)

    #This part constructs a CSV file by connecting the first element of each line with all the other elements of the same line.
    with open('output.csv', 'w') as f:

        sys.stdout = f #Record of print initialization

        for key, value in prim_MST.items():
            print(f"{key}", end=" ")
                
            for list in value:
                print(f"{list[0]}", end=" ")
            
            print("")

        sys.stdout = original_stdout #Finishing print initialization