import random as rd
import persons2 as pdata
import names as nms
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


pers = pdata.Persons
anglo = pdata.AngloSaxon




class PeopleGen:
    temp_list = pers.people_list.copy()

    def __init__(self):
        self.family_graph = nx.DiGraph()
        self.gpp = None

    def person_gen(self, age_bound_younger=False, age_bound_older=False, male=False, female=False, **kwargs):
        # set instance
        person = anglo(pers.unique_id_num)
        # set gender
        if not male and not female:
            choose_gender = rd.choice(['Male', 'Female'])
            if choose_gender == 'Male':
                male = True
            elif choose_gender == 'Female':
                female = True
        if male:
            person.set_gender('Male')
            person.set_fname(rd.choice(nms.male_anglo_names))
        elif female:
            person.set_gender('Female')
            person.set_fname(rd.choice(nms.female_anglo_names))
        # set age
        if age_bound_younger:
            if 'father' in kwargs and 'mother' in kwargs:
                person.set_age((kwargs['father'].get_age + kwargs['mother'].get_age) / 2 - rd.randint(16, 30))
            elif 'father' in kwargs and 'mother' not in kwargs:
                person.set_age(kwargs['father'].get_age - rd.randint(16, 30))
            elif 'mother' in kwargs and 'father' not in kwargs:
                person.set_age(kwargs['mother'].get_age - rd.randint(16, 30))
        if age_bound_older:
            if 'child' in kwargs:
                person.set_age(kwargs['child'].get_age + rd.randint(16, 30))
        else:
            person.set_age(rd.randint(18, 70))
        # set immediate family
        # parents
        if 'father' in kwargs:
            if kwargs['father']:
                person.set_father(kwargs['father'])
                kwargs['father'].set_children(person)
        if 'mother' in kwargs:
            if kwargs['mother']:
                person.set_mother(kwargs['mother'])
                kwargs['mother'].set_children(person)
        # siblings
        if 'mother' in kwargs:
            if kwargs['mother'].get_children:
                for children in kwargs['mother'].get_children:
                    if children not in person.get_siblings:
                        person.set_siblings(children)
                    if person not in children.get_siblings:
                        children.set_siblings(person)
        if 'father' in kwargs:
            if kwargs['father'].get_children:
                for children in kwargs['father'].get_children:
                    if children not in person.get_siblings:
                        person.set_siblings(children)
                    if person not in children.get_siblings:
                        children.set_siblings(person)
        # health gen
        if person.get_age > 55:
            person.set_health(rd.randint(0, 50))
        elif person.get_age < 55:
            person.set_health(rd.randint(25, 100))
        # add instance to list
        pers.people_list.append(person)
        return person

    def family_gen(self, subject):
        pg = PeopleGen
        if not subject.get_father:
            father = pg.person_gen(self, age_bound_older=True, child=subject, male=True)
            subject.set_father(father)
        else:
            father = subject.get_father
        if not subject.get_mother:
            mother = pg.person_gen(self, age_bound_older=True, child=subject, female=True)
            subject.set_mother(mother)
        else:
            mother = subject.get_mother
        siblings_trigger1 = rd.randint(1, 100)
        if siblings_trigger1 > 50:
            sibling1 = pg.person_gen(self, age_bound_younger=True, father=father, mother=mother)
            father.set_children(sibling1)
            mother.set_children(sibling1)
            sibling1.set_siblings(subject)
            subject.set_siblings(sibling1)


    def founding_sib_gen(self, f, m):
        sibling_amnt_t = rd.randint(0, 5)
        if sibling_amnt_t > 3:
            sibling_amt = rd.randint(0, 5)
        else:
            sibling_amnt_t = rd.randint(0, 2)
        for siblings in range(sibling_amnt_t):
            pass








ppl = PeopleGen()
for x in range(20):
    ppl.person_gen()
for ps in range(50):
    yerd = rd.choice(pers.people_list)
    ppl.family_gen(yerd)

families = {'id': [], 'father':[], 'mother': [], 'sex': []}
for persons in pers.people_list:
    families['id'].append(persons.unique_id)
    if not persons.get_father:
        families['father'].append(0)
    else:
        families['father'].append(persons.get_father.get_unique_id)
    if not persons.get_mother:
        families['mother'].append(0)
    else:
        families['mother'].append(persons.get_mother.get_unique_id)
    if persons.get_gender == 'Male':
        families['sex'].append(1)
    elif persons.get_gender == 'Female':
        families['sex'].append(2)
df_families = pd.DataFrame(families)
df_families.to_csv('families.csv')
print(df_families)
print(families)
dog = rd.choice(pers.people_list)
a = dog.get_family()
b = dog.retrieve_pc(relations=a)
print('yerd')
print(b)
print(a)
df_family = pd.DataFrame(a)
df_family.to_csv('family.csv', index=False)

# print(pers.f_trees.nodes)
# nx.draw_networkx(pers.f_trees)
