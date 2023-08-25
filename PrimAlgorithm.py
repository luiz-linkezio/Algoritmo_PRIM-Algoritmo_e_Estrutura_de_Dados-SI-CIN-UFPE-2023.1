import random

class PrimAlgorithm:
    def __init__(self):
       self.MST = {} 

    #creates a MST
    def MST_creation(self, graph, current_vertex=0):
        visit_dic = {} #list of elements to be visited
        weight_list = [] #weights to be checked whether or not they should be removed from the visit dictionary
        time_to_find_cure = 0 #time to find the cure
        deaths = 0 #number of deaths

        self.MST[current_vertex] = [] #adds the initial vertex to the graph of the minimum spanning tree
        
        #adds up to the last vertex
        for vertex in range(len(graph)-1): 
            #adds future visits
            for neighboring_vertex, weight in graph[current_vertex]: 
                if weight not in visit_dic and neighboring_vertex not in self.MST: #new weight and vertex 
                    visit_dic[weight] = [[current_vertex, neighboring_vertex]]
                elif weight in visit_dic and neighboring_vertex not in self.MST: #old weight and new vertex
                    visit_dic[weight].append([current_vertex, neighboring_vertex])

            #check out future visits
            for weight in visit_dic:
                for vertex1, vertex2 in visit_dic[weight]:
                    if vertex1 in self.MST and vertex2 in self.MST: #check if both vertex have been visited 
                        visit_dic[weight].remove([vertex1,vertex2]) 
                        if weight not in weight_list:
                            weight_list.append(weight) #adds modified weight to the list of weights

            #updates weight list
            weight_list = self.remove_weight_visit(weight_list, visit_dic)

            #sort to find the lowest weight
            sorted_visit_dic = min(visit_dic) 
            visit_weight = sorted_visit_dic

            #makes vertex changes 
            visited_vertex, current_vertex = visit_dic[visit_weight][0]
            visit_dic[visit_weight].remove([visited_vertex,current_vertex])
            if visit_weight not in weight_list:
                weight_list.append(visit_weight) #adds modified weight to the list of weights
            
            #updates weight list
            weight_list = self.remove_weight_visit(weight_list, visit_dic)
                
            self.MST[current_vertex] = [] #adds a new vertex to the MST

            #adds links between vertex in the MST
            self.MST[visited_vertex].append([current_vertex, visit_weight]) 
            self.MST[current_vertex].append([visited_vertex, visit_weight]) 

            #Random things treatment
            time_to_find_cure += 60*visit_weight*(random.uniform(0.75, 1.25)) #Total minutes to find the cure counter
            deaths += random.randint(9000, 27000)/(len(self.MST)/10) #Total number of deaths counter
            variant_chance = random.uniform(0.1,100.0)
            if variant_chance <= 0.3:
                deaths *= 1.25
                time_to_find_cure *= 1.7
            immunity_chance = random.uniform(0.01,100.0)
            if immunity_chance <= 0.025:
                time_to_find_cure /= 2

        return self.MST, time_to_find_cure, int(deaths)
    
    #updates weight list
    def remove_weight_visit(self, weight_list, visit_dic): 
        weight_removed_list = [] #list of weights already removed from the visit dictionary

        #clear all empty weights
        for weight in weight_list:
            if weight in visit_dic:
                if visit_dic[weight] == []:
                    visit_dic.pop(weight)
                    weight_removed_list.append(weight)

        for weight in weight_removed_list:
            weight_list.remove(weight)

        return weight_list