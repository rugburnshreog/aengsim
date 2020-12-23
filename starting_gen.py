import random as rd
import persons2 as pdata
import names as nms
import networkx as nx


pers = pdata.Persons
anglo = pdata.AngloSaxon


class StartingGen:
    temp_list = pers.people_list.copy()

    def __init__(self):
        pass

    def start_people_gen(self):
        male_count = rd.randrange(6, 11)
        female_count = rd.randrange(6, 11)
        for m_count in range(male_count):
            current_p = anglo(pers.unique_id_num)
            current_p.set_fname(rd.choice(nms.male_anglo_names))
            current_p.set_age(rd.randrange(18, 65))
            current_p.set_gender('Male')
            current_p.set_health(rd.randrange(80, 100))
            pers.people_list.append(current_p)
        for f_count in range(female_count):
            current_p = anglo(pers.unique_id_num)
            current_p.set_fname(rd.choice(nms.female_anglo_names))
            current_p.set_age(rd.randrange(18, 65))
            current_p.set_gender('Female')
            current_p.set_health(rd.randrange(80, 100))
            pers.people_list.append(current_p)


    def starting_relation_gen(self):
        for count in range(rd.randrange(50, 100)):
            potential_relations = ['father', 'mother', 'sister', 'brother', 'daughter', 'son']
            temp_list = pers.people_list.copy()
            p1 = rd.choice(temp_list)
            p2 = rd.choice(temp_list)
            while p2 == p1:  # searches until it finds two dissimilar matches
                p2 = rd.choice(temp_list)
            temp_list.remove(p1)
            temp_list.remove(p2)
            pot_relation = rd.choice(potential_relations)
            if pot_relation == 'father' and p1.get_father is not None:  # only 1 father
                potential_relations.remove('father')
                pot_relation = rd.choice(potential_relations)
            if pot_relation == 'mother' and p1.get_mother is not None:  # only 1 mother
                potential_relations.remove('mother')
                pot_relation = rd.choice(potential_relations)
            if pot_relation == 'father' and p1.get_father is None and p2.get_children == []:  # no father = true, generate father
                StartingGen.choice_father(self, p1, p2, temp_list)

    def choice_father(self, p1, p2, temp_list):
        add_relation = pers.f_trees.add_edge
        while p2.get_gender == 'Female':  # guarantees male for father
            p2 = rd.choice(temp_list)
        if (p1.get_age + 16) < p2.get_age:
            p1.set_father(p2)
            pers.add_f_tree_node(p1)
            pers.set_node_position(p1)
            pers.add_f_tree_node(p2)
            pers.set_node_position(p2)
            add_relation(p2.get_unique_id, p1.get_unique_id)
            pers.f_trees.edges[p2.get_unique_id, p1.get_unique_id]['Relation'] = 'Parent'
            p2.set_children(p1)
            if p1.get_mother is None:
                p3 = rd.choice(temp_list)
                retrieved_index_error = False
                while p3.get_gender == 'Male' or (p1.get_age + 16) > p3.get_age or p3.get_children != []:
                    if retrieved_index_error:
                        break
                    try:
                        p3 = rd.choice(temp_list)
                        temp_list.remove(p3)
                    except IndexError as idxerr:
                        retrieved_index_error = True
                        print(idxerr)
                p1.set_mother(p3)
                pers.add_f_tree_node(p3)
                pers.set_node_position(p3)
                add_relation(p3.get_unique_id, p1.get_unique_id)
                pers.f_trees.edges[p3.get_unique_id, p1.get_unique_id]['Relation'] = 'Parent'
                new_x_value = ((nx.get_node_attributes(pers.f_trees, 'pos')[p2.get_unique_id][0] +
                  nx.get_node_attributes(pers.f_trees, 'pos')[p3.get_unique_id][0]) / 2)
                new_y_value = nx.get_node_attributes(pers.f_trees, 'pos')[p2.get_unique_id][1] - .35
                nx.set_node_attributes(pers.f_trees, {p1.get_unique_id:{'pos': (new_x_value, new_y_value)}})
                p3.set_children(p1)
                if p2.get_married is None and p3.get_married is None:  # if both are unmarried set marriage
                    p2.set_married(p3)
                    p3.set_married(p2)
                    add_relation(p3.get_unique_id, p2.get_unique_id)
                    pers.f_trees.edges[p3.get_unique_id, p2.get_unique_id]['Relation'] = 'Marriage'

    def more_children_gen(self, p1, p2, p3, temp_list):
        pass
