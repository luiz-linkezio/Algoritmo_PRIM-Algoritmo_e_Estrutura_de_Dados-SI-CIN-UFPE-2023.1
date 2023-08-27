class GeneAssociations:
    def __init__(self):
       self.graph = {}

    def add_gene_associations(self, infection_db):
        for index, data in infection_db.iterrows():
            gene1 = int(data['Gene 1'])
            gene2 = int(data['Gene 2'])
            infection_degree = data['Infection Degree']

            if gene1 not in self.graph:
                self.graph[gene1] = []
            if gene2 not in self.graph:
                self.graph[gene2] = []
            self.graph[gene1].append([gene2, infection_degree])
            self.graph[gene2].append([gene1, infection_degree])