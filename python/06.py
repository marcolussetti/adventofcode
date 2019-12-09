#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open('../inputs/06', 'r') as f:
    file_lines = f.readlines()
input_lines = [line.strip().split(')') for line in file_lines]


# ## Part 1

# In[2]:


def find_in_input(item):
    return [inner for inner, outer in input_lines if outer == item]


# In[3]:


def extract_chain(input_i):
    queue = list(set(find_in_input(input_i)))
    total = list(set(queue))
    while len(queue) > 0:
        for item in queue:
            inner_items = set(find_in_input(item))
            total = set(total) | inner_items
            queue = set(queue) | inner_items
            queue.remove(item)
    return total


# In[4]:


keys = set([outer for inner, outer in input_lines])


# In[5]:


mappings = {key: extract_chain(key) for key in keys}
sum([len(item) for key, item in mappings.items()])


# ## Part 2

# In[6]:


def find_paths(current):
    inner = find_in_input(current[-1])
    if len(inner) > 0:
        current.append(inner[0])
        current = find_paths(current)

    return current


# In[7]:


path_from_you = find_paths(['YOU'])
path_from_san = find_paths(['SAN'])


# In[8]:


intersections = {element: (path_from_san.index(element) - 1) + (i - 1)
                 for i, element in enumerate(path_from_you) if element in path_from_san}


# In[9]:


min([val for key, val in intersections.items()])

