import pandas
from scripts.time_config import time_config, time_printer
from scripts.GeneAssociations import *
from scripts.PrimAlgorithm import *
from tkinter import *

class Main:
    #Classes initializations
    gene_associations = GeneAssociations()
    prim = PrimAlgorithm()

    #Turn CSV into DataFrame
    infection_db = pandas.read_csv('database.csv')

    #Database collected
    print('The following database shows the functional associations between the genes collected to find a cure:')
    print(infection_db)

    #Create graph
    gene_associations.add_gene_associations(infection_db)
    infection_graph = gene_associations.graph

    #Prim Algorithm
    print(f'Enter the sample index to start the analysis in a range from 0 to {len(infection_graph)-1}:')
    initial_vertex = int(input())
    prim_MST, time_to_find_cure, deaths = prim.MST_creation(infection_graph, initial_vertex) #Prim Algorithm: MST creation and the time calculation for find a cure
    
    #Time treatment
    years, days, hours, minutes, seconds = time_config(time_to_find_cure)
    
    #Prints
    print(f"Unfortunately, during this pandemic {deaths} people died.")
    time_printer(years, days, hours, minutes, seconds)
    if days <= 0:
        days = 1
    print(f"As a result, approximately {int(deaths/days)} people died per day while the cure was being researched.")

    import subprocess

    # Caminho para o executável do Gephi
    gephi_path = 'C:\\Arquivos de Programas\\Gephi-0.10.1\\bin\\gephi64.exe'

    # Caminho para o arquivo CSV que você deseja abrir no Gephi
    csv_file_path = 'output.csv'

    try:
        # Use o subprocess para abrir o arquivo CSV no Gephi
        subprocess.run([gephi_path, "--open", csv_file_path])
    except FileNotFoundError:
        print("Gephi não encontrado. Verifique o caminho do executável.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")