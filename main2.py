import persons2 as pdata
import random as rd
import starting_gen as st
import matplotlib.pyplot as plt
import networkx as nx
import graphviz as gv

pers = pdata.Persons
anglo = pdata.AngloSaxon
start_gen = st.StartingGen()

start_gen.start_people_gen()
for people in pers.people_list:
    print(people.__dict__)

start_gen.starting_relation_gen()

for persons in pers.people_list:
    print(persons.get_status)
print(pers.f_trees.nodes)
pos1 = nx.get_node_attributes(pers.f_trees, 'pos')
nx.draw_networkx_nodes(pers.f_trees, pos1, node_size=100, node_shape='s')
f_names = nx.get_node_attributes(pers.f_trees, 'attr_dict')
id_corr = []
name_corr = []
for k, v in f_names.items():
    id_corr.append(k)
    for inner_k, inner_v in v.items():
        if inner_k == 'fname':
            name_corr.append(inner_v)
id_name = dict(zip(id_corr, name_corr))
print(id_name)
marriage_list = [edges for edges in pers.f_trees.edges(data=True) if 'Relation' in edges[2] if edges[2]['Relation'] == 'Marriage']
parent_child_list = [edges for edges in pers.f_trees.edges(data=True) if 'Relation' in edges[2] if edges[2]['Relation'] == 'Parent']
print(marriage_list)
nx.draw_networkx_edges(pers.f_trees, pos1, width=2, connectionstyle='angle,angleA=-90,angleB=180,rad=5', edgelist=marriage_list, arrows=False, edge_color='Red')
nx.draw_networkx_edges(pers.f_trees, pos1, width=2, connectionstyle='angle,angleA=-90,angleB=180,rad=5', edgelist=parent_child_list, edge_color='Blue')
# print(pos1)
# for p in pos1:
#     pos1[p] = (pos1[p][0], pos1[p][1]+.02)
nx.draw_networkx_labels(pers.f_trees, pos1, font_size=8, bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'), labels=id_name)
plt.show()

for people in pers.people_list:
    print(people.get_children)

