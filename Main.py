import pandas
from GeneAssociations import GeneAssociations

"""!!!LEMBRETE!!!
1. Fazer comentários (colocar em inglês)
2. Criar pastas diferentes para as classes
3. Chamar funções e fatores gerais por essa classe Main
4. Para rodar com biblioteca pandas faça a seguinte chamada no terminal:
pip install pandas
E tambem instale o puglin 'anaconda terminal' aqui no VSCode"""

class Main:
    #Turn CSV into DataFrame
    infection_db = pandas.read_csv('database.csv') #essa é a nossa base completa
    infection_db = pandas.read_csv('db.csv') #pode usar essa pra os testes menores

    #Database collected
    print('The following database shows the functional associations between the genes collected to find a cure:')
    print(infection_db)

    #Create graph
    gene_associations = GeneAssociations()
    gene_associations.add_gene_associations(infection_db)