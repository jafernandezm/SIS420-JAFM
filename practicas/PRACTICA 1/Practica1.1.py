#!/usr/bin/env python
# coding: utf-8

# In[5]:



#ejemplo de conjuntos
group_a = set(['Ana', 'Marcos', 'Carlos', 'Mario'])
group_b = {'Ana', 'Pedro', 'Carlos', 'Antonio'}
group_c = {'Ana', 'Antonio', 'Marcos', 'Pepe'}

all_students = group_a.union(group_b).union(group_c)
all_students
a_and_b = group_a.intersection(group_b)
a_and_b


# In[14]:


#listas 
sea_creatures = ['shark', 'cuttlefish', 'squid',
'mantis shrimp', 'anemone']
print(sea_creatures)
print(sea_creatures[1])
sea_creatures[0] = 'shark'
sea_creatures[1] = 'cuttlefish'
sea_creatures[2] = 'squid'
sea_creatures[3] = 'mantis shrimp'
sea_creatures[4] = 'anemone'
print(sea_creatures)
#print(sea_creatures[18])
print(sea_creatures[:3])
print(sea_creatures[2:])
print(sea_creatures[-4:-2])
print(sea_creatures[-3:])

#numero
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers[1:11:2])


# In[ ]:




