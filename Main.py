import pandas
import time
from time_config import time_config, time_printer
from GeneAssociations import GeneAssociations
from PrimAlgorithm import PrimAlgorithm

"""!!!LEMBRETE!!!
1. Fazer comentários (colocar em inglês)
2. Criar pastas diferentes para as classes
3. Chamar funções e fatores gerais por essa classe Main
4. Para rodar com biblioteca pandas faça a seguinte chamada no terminal:
pip install pandas
E tambem instale o puglin 'anaconda terminal' aqui no VSCode"""

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
    start_time = time.time() #Stopwatch initialization
    gene_associations.add_gene_associations(infection_db)
    infection_graph = gene_associations.graph

    #Prim Algorithm
    prim_MST, time_to_find_cure, deaths = prim.MST_creation(infection_graph) #Prim Algorithm: MST creation and the time calculation for find a cure
    end_time = time.time() #Stopwatch stop
    
    #Time treatment
    years, days, hours, minutes, seconds = time_config(time_to_find_cure)
    
    #Prints
    print(prim_MST)
    print(f"The time spent to analyze the database was: around {round((end_time - start_time), 3)} seconds.")
    print(time_to_find_cure)
    print(f"During this pandemic, unfortunately {deaths} people died")
    time_printer(years, days, hours, minutes, seconds)
    if days <= 0:
        days = 1
    print(f"This mean that around {round(deaths/days)} people died per day while the cure was be in researching.")