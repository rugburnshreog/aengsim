def founder_gen(self):
    PeopleGen.family_graph_gen(self, self.family_graph)
    founding_f = anglo(pers.unique_id_num)
    founding_f.set_f_graph(self.family_graph)
    founding_f.set_age(rd.randrange(65, 80))
    founding_f.set_gender('Male')
    dead_alive_t = rd.randrange(0, 5)
    if dead_alive_t > 4:
        founding_f.set_health(rd.randrange(1, 25))
    else:
        founding_f.set_health(0)
    founding_f.set_fname(rd.choice(nms.male_anglo_names))
    pers.people_list.append(founding_f)
    pers.add_f_tree_node(founding_f)
    founding_m = anglo(pers.unique_id_num)
    founding_m.set_f_graph(self.family_graph)
    founding_m.set_age(rd.randrange(65, 80))
    founding_m.set_gender('Female')
    dead_alive_t = rd.randrange(0, 5)
    if dead_alive_t > 4:
        founding_m.set_health(rd.randrange(1, 25))
    else:
        founding_m.set_health(0)
    founding_m.set_fname(rd.choice(nms.female_anglo_names))
    pers.people_list.append(founding_m)
    pers.add_f_tree_node(founding_m)
    for x in range(10):
        PeopleGen.person_gen(self, age_bound_younger=False, age_bound_older=True, mother=founding_m, father=founding_f,
                             child=founding_f)


# graph
    def add_f_tree_node(self):
        graph = self.f_graph
        graph.add_node(self.unique_id, attr_dict=
                                    {'Gender': self.gender,
                                     'Age': self.age,
                                     'Culture': self.culture,
                                     'fname': self.fname,
                                     'Marriage': self.married,
                                     'Generation': self.generation
                                     })

    def set_node_position(self):
        global x_pos
        global y_pos
        new_y_value = y_pos
        new_x_value = x_pos + 2
        x_pos += 2
        nx.set_node_attributes(self.f_graph, {self.get_unique_id:{'pos': (new_x_value, new_y_value)}})

    @property
    def get_generation(self):
        return self.generation

    def set_generation(self, generation):
        self.generation = generation

    @property
    def get_f_graph(self):
        return self.f_graph

    def set_f_graph(self, graph):
        self.f_graph = graph

    def family_graph_gen(self, family_graph):
        pers.unique_f_num += 1
        pers.family_trees[pers.unique_f_num] = family_graph

    self.generation = 0
    self.f_graph = None