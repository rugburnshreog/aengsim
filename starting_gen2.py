import random as rd
import persons2 as pdata
import names as nms
import networkx as nx
import matplotlib.pyplot as plt

pers = pdata.Persons
anglo = pdata.AngloSaxon




class PeopleGen:
    temp_list = pers.people_list.copy()
    gpp = 2

    def __init__(self):
        self.family_graph = nx.DiGraph()

    def family_graph_gen(self, family_graph):
        pers.unique_f_num += 1
        pers.family_trees[pers.unique_f_num] = family_graph

    def founder_gen(self):
        test_g = nx.DiGraph()
        PeopleGen.family_graph_gen(self, self.family_graph)
        founding_f = anglo(pers.unique_id_num)
        founding_f.set_f_graph(self.family_graph)
        founding_f.set_age(rd.randrange(18, 65))
        founding_f.set_gender('Male')
        founding_f.set_health(rd.randrange(80, 100))
        founding_f.set_fname(rd.choice(nms.male_anglo_names))
        pers.people_list.append(founding_f)
        pers.add_f_tree_node(founding_f)
        print(founding_f.get_f_graph.nodes)





ppl = PeopleGen()
ppl.founder_gen()
# print(pers.f_trees.nodes)
# nx.draw_networkx(pers.f_trees)
