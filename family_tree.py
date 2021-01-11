import matplotlib.pyplot as plt
import networkx as nx
import starting_gen2 as stg
import graphviz as gv
import os
import persons2

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz 2.44.1/bin'


class FamilyTree:
    graph_n = 0

    def __init__(self, gdata, ipnodes):
        self.gdata = gdata
        self.fgraph = gv.Digraph(name=FamilyTree.graph_n, filename='yep.gv', strict=True)
        self.ipnodes = ipnodes[0]
        self.invis_parent_nodes = ipnodes[1]

        FamilyTree.graph_n += 1

    def print_graph(self):
        print(self.fgraph.source)
        self.fgraph.render()

    def nodes_and_edges(self):
        potential_parents = [parent_ids['parent_id'] for parent_ids in self.gdata if parent_ids['parent_id'] != 0]
        filtered_parents = []
        [filtered_parents.append(parents) for parents in potential_parents if parents not in filtered_parents]
        passed_parents = []
        for pot_parents in filtered_parents:
            self.fgraph.node(str(pot_parents), shape='point', width='0', splines='ortho')
        for row in self.gdata:
            if row['gender'] == 1:
                self.fgraph.node(str(row['id']), shape='circle', splines='ortho')
            elif row['gender'] == 2:
                self.fgraph.node(str(row['id']), shape='square', splines='ortho')
            if row['father_id'] != 0:
                self.fgraph.edge(str(row['parent_id']), str(row['id']), arrowhead='none', splines='ortho')
        for invis_parent_nodes in self.invis_parent_nodes:
            self.fgraph.node(str(invis_parent_nodes[0]), shape='point', width='0', splines='ortho')
            self.fgraph.edge(str(invis_parent_nodes[0]), str(invis_parent_nodes[1]))
            # for parents in filtered_parents:
            #     for people in self.gdata:
            #         if row['id'] + people['id'] == parents:
            #             self.fgraph.edge(str(row['id']), str(parents), splines='ortho')
            #     f_m = persons2.depair(parents)
            #     father = f_m[0]
            #     if father not in passed_parents:
            #         self.fgraph.edge(str(father), str(parents), splines='ortho')
            #         passed_parents.append(father)
            #     mother = f_m[1]
            #     if mother not in passed_parents:
            #         self.fgraph.edge(str(mother), str(parents), splines='ortho')
            #         passed_parents.append(mother)

    def reshape_nodes(self):
        self.fgraph.node_attr['peripheries'] = '2'

    def reshape_edges(self):
        self.fgraph.edge_attr['splines'] = 'ortho'


ft = FamilyTree(stg.a, stg.b)
ft.nodes_and_edges()
ft.print_graph()
