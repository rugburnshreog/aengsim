import networkx as nx
import math
x_pos = 0
y_pos = 1

def pair(k1, k2, safe=True):
    """
    Cantor pairing function
    http://en.wikipedia.org/wiki/Pairing_function#Cantor_pairing_function
    """
    z = int(0.5 * (k1 + k2) * (k1 + k2 + 1) + k2)
    if safe and (k1, k2) != depair(z):
        raise ValueError("{} and {} cannot be paired".format(k1, k2))
    return z


def depair(z):
    """
    Inverse of Cantor pairing function
    http://en.wikipedia.org/wiki/Pairing_function#Inverting_the_Cantor_pairing_function
    """
    w = math.floor((math.sqrt(8 * z + 1) - 1)/2)
    t = (w**2 + w) / 2
    y = int(z - t)
    x = int(w - y)
    # assert z != pair(x, y, safe=False):
    return x, y

class Persons:
    unique_id_num = 1
    people_list = []
    alive_people = []
    deceased_people = []

    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.fname = None
        self.nickname = None
        self.lname = None
        self.age = None
        self.gender = None
        self.health = None
        self.culture = None
        self.married = None
        self.father = None
        self.mother = None
        self.children = []
        self.siblings = []


        Persons.unique_id_num += 1

    @property
    def get_status(self):
        status = []
        if self.unique_id >= 0:
            status.append(self.unique_id)
        if self.fname:
            status.append(self.fname)
        if self.nickname:
            status.append(self.fname)
        if self.lname:
            status.append(self.lname)
        if self.age:
            status.append(self.age)
        if self.gender:
            status.append(self.gender)
        if self.health:
            status.append(self.health)
        if self.culture:
            status.append(self.culture)
        if self.married:
            status.append('married to:' + str(self.married.get_unique_id))
        if self.father:
            status.append('father:' + str(self.father.get_unique_id))
        if self.mother:
            status.append('mother:' + str(self.mother.get_unique_id))
        if self.siblings:
            status.append(self.siblings)
        if self.children:
            status.append(self.show_children)
        if self.generation:
            status.append(self.generation)
        return status

    @property
    def show_children(self):
        childs = []
        for child in self.children:
            childs.append(child.get_unique_id)
        return childs

    @property
    def get_unique_id(self):
        return self.unique_id

    @property
    def get_fname(self):
        return self.fname

    def set_fname(self, fname):
        self.fname = fname

    @property
    def get_nickname(self):
        return self.nickname

    def set_nickname(self, nickname):
        self.nickname = nickname

    @property
    def get_lname(self):
        return self.lname

    def set_lname(self, lname):
        self.lname = lname

    @property
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    @property
    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    @property
    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    @property
    def get_culture(self):
        return self.culture

    def set_culture(self, culture):
        self.culture = culture

    @property
    def get_married(self):
        return self.married

    def set_married(self, married):
        self.married = married

    @property
    def get_children(self):
        return self.children

    def set_children(self, children):
        self.children.append(children)

    @property
    def get_siblings(self):
        return self.siblings

    def set_siblings(self, siblings):
        self.siblings.append(siblings)

    @property
    def get_father(self):
        return self.father

    def set_father(self, father):
        self.father = father

    @property
    def get_mother(self):
        return self.mother

    def set_mother(self, mother):
        self.mother = mother

    def get_family(self, passed_people=None, relations=None):
        if passed_people is None:
            passed_people = []
        if relations is None:
            relations = []
        if self not in passed_people:
            passed_people.append(self)
        relations_dict = {}
        if self.father:
            father = self.father
            father_id = father.get_unique_id
        else:
            father_id = 0
        if self.mother:
            mother = self.mother
            mother_id = mother.get_unique_id
        else:
            mother_id = 0
        if self.gender == 'Male':
            gender = 1
        else:
            gender = 2
        relations_dict['id'] = self.unique_id
        relations_dict['father_id'] = father_id
        relations_dict['mother_id'] = mother_id
        relations_dict['parent_id'] = pair(father_id, mother_id)
        relations_dict['gender'] = gender
        relations_dict['children_id'] = 0
        relations_dict['pobject'] = self
        if relations_dict['id'] not in relations:
            relations.append(relations_dict)
        if self.father:
            if self.father not in passed_people:
                self.father.get_family(passed_people=passed_people, relations=relations)
        if self.mother:
            if self.mother not in passed_people:
                self.mother.get_family(passed_people=passed_people, relations=relations)
        if self.siblings:
            for sibling in self.siblings:
                if sibling not in passed_people:
                    sibling.get_family(passed_people=passed_people, relations=relations)
        if self.children:
            for child in self.children:
                if child not in passed_people:
                    child.get_family(passed_people=passed_people, relations=relations)
        return relations

    def retrieve_pc(self, relations):
        depaired_parents = []
        invis_node_pairs = []
        for parents in relations:
            if parents['parent_id'] > 0:
                parents_map = []
                tupled_parents = depair(parents['parent_id'])
                for tup_par in tupled_parents:
                    parents_map.append(tup_par)
                parents_map.append(parents['parent_id'])
                depaired_parents.append(parents_map)
        for parents in depaired_parents:
            father = parents[0]
            mother = parents[1]
            parent_id = parents[2]
            invis_f_node = pair(father, parent_id)
            invis_m_node = pair(mother, parent_id)
            invis_node_pairs.append((invis_f_node, parent_id))
            invis_node_pairs.append((invis_m_node, parent_id))
            for people in relations:
                if father == people['id']:
                    people['children_id'] = parent_id
                    people['invis_f_node'] = invis_f_node
                elif mother == people['id']:
                    people['children_id'] = parent_id
                    people['invis_m_node'] = invis_m_node
                else:
                    continue
        return (depaired_parents, invis_node_pairs)

    def retrieve_child_pnodes(self, relations):
        pass









class AngloSaxon(Persons):
    culture = 'Anglo-Saxon'

    def __init__(self, unique_id):
        super().__init__(unique_id)
        self.culture = AngloSaxon.culture



