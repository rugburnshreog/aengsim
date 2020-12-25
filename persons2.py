import networkx as nx
x_pos = 0
y_pos = 1


class Persons:
    unique_id_num = 0
    unique_f_num = 0
    people_list = []
    f_trees = nx.DiGraph()
    family_trees = {}

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
        self.f_graph = None


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

    @property
    def get_f_graph(self):
        return self.f_graph

    def set_f_graph(self, graph):
        self.f_graph = graph


    def add_f_tree_node(self):
        graph = self.f_graph
        graph.add_node(self.unique_id, attr_dict=
                                    {'Gender': self.gender,
                                     'Age': self.age,
                                     'Culture': self.culture,
                                     'fname': self.fname,
                                     'Marriage': self.married,
                                     'Level': 10
                                     })
        Persons.f_trees.add_node(self.unique_id, attr_dict=
                                    {'Gender': self.gender,
                                     'Age': self.age,
                                     'Culture': self.culture,
                                     'fname': self.fname,
                                     'Marriage': self.married,
                                     'Level': 10
                                     })
        print(Persons.f_trees.nodes)
        print(self.f_graph.nodes)

    def set_node_position(self):
        global x_pos
        global y_pos
        new_y_value = y_pos
        new_x_value = x_pos + 2
        x_pos += 2
        nx.set_node_attributes(self.f_graph, {self.get_unique_id:{'pos': (new_x_value, new_y_value)}})








class AngloSaxon(Persons):
    culture = 'Anglo-Saxon'

    def __init__(self, unique_id):
        super().__init__(unique_id)
        self.culture = AngloSaxon.culture