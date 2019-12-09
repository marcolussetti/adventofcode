#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools


# In[2]:


with open('../inputs/02', 'r') as f:
    file_lines = f.readlines()
input_lines = [int(line.strip()) for line in file_lines[0].split(",")]


# ## Part 1

# In[3]:


def run_program(values):
    lines = values.copy()
    current_op = 0
    while lines[current_op] != 99:
        op = lines[current_op]
        first = lines[current_op+1]
        second = lines[current_op+2]
        third = lines[current_op+3]
        first_val = lines[first]
        second_val = lines[second]

        if op == 99:
            break
        elif op == 1:
            lines[third] = first_val + second_val
        elif op == 2:
            lines[third] = first_val * second_val
        current_op = current_op + 4

    return lines


# In[4]:


# Sample value(s)
run_program([2, 4, 4, 5, 99, 0])


# In[5]:


# Solve for Part 1
modified_input = input_lines.copy()
modified_input[1] = 12
modified_input[2] = 2

result_1 = run_program(modified_input)
result_1[0]


# ## Part 2

# In[6]:


def generate_lines(input_values, noun, verb):
    new_values = input_values.copy()
    new_values[1] = noun
    new_values[2] = verb

    return new_values


# In[7]:


nouns = list(range(1, 1000))
verbs = list(range(1, 1000))
combos = list(itertools.product(*[nouns, verbs]))
# combos


# In[8]:


for noun, verb in combos:
    generated_lines = generate_lines(input_lines, noun, verb)
    try:
        result = run_program(generated_lines)
        result_value = result[0]
    except:
        continue

    if result_value == 19690720:
        print("Noun: {}. Verb: {}".format(noun, verb))
        break


# In[9]:


100 * noun + verb

