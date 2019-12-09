#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools


# In[2]:


with open('../inputs/05', 'r') as f:
    file_lines = f.readlines()
input_lines = [int(line.strip()) for line in file_lines[0].split(",")]


# ## Part 1

# In[3]:


def execute_program(program, input_value):
    p = program.copy()
    i = 0
    while p[i] != 99:
        op = int(str(p[i])[-2:])
        modes = [int(char) for char in str(p[i])[:-2].zfill(3)][::-1]

        if op == 1 or op == 2:  # Compute variables
            variables = [
                p[i+1] if modes[0] else p[p[i+1]],
                p[i+2] if modes[1] else p[p[i+2]]
            ]

        if op == 1:  # Sum
            p[p[i+3]] = variables[0] + variables[1]
            i += 4
        elif op == 2:  # Multiplication
            p[p[i+3]] = variables[0] * variables[1]
            i += 4
        elif op == 3:  # Input
            p[p[i+1]] = input_value
            i += 2
        elif op == 4:  # Output
            print(p[p[i+1]])
            i += 2

    return p


# In[4]:


# Sample value(s)
test = execute_program([1002, 4, 3, 4, 33], 1)


# In[5]:


# Sample value(s)
test = execute_program([1101, 100, -1, 4, 0], 1)


# In[6]:


# Solve for Part 1
result_1 = execute_program(input_lines, 1)


# ## Part 2

# In[7]:


def execute_program_two(program, input_value):
    p = program.copy()
    i = 0
    while p[i] != 99:
        op = int(str(p[i])[-2:])
        modes = [int(char) for char in str(p[i])[:-2].zfill(3)][::-1]

        if op != 3 and op != 4:  # Compute variables
            variables = [
                p[i+1] if modes[0] else p[p[i+1]],
                p[i+2] if modes[1] else p[p[i+2]]
            ]

        if op == 1:  # Sum
            p[p[i+3]] = variables[0] + variables[1]
            i += 4
        elif op == 2:  # Multiplication
            p[p[i+3]] = variables[0] * variables[1]
            i += 4
        elif op == 3:  # Input
            p[p[i+1]] = input_value
            i += 2
        elif op == 4:  # Output
            print(p[p[i+1]])
            i += 2
        elif op == 5:
            i = variables[1] if variables[0] else i + 3
        elif op == 6:
            i = i + 3 if variables[0] else variables[1]
        elif op == 7:
            p[p[i+3]] = int(variables[0] < variables[1])
            i += 4
        elif op == 8:
            p[p[i+3]] = int(variables[0] == variables[1])
            i += 4

    return p


# In[8]:


test = execute_program_two([3,9,8,9,10,9,4,9,99,-1,8], 5)


# In[9]:


test = execute_program_two([3,9,7,9,10,9,4,9,99,-1,8], 9)


# In[10]:


test = execute_program_two([3,3,1108,-1,8,3,4,3,99], 8)


# In[11]:


test = execute_program_two([3,3,1107,-1,8,3,4,3,99], 8)


# In[12]:


test = execute_program_two([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002,
               21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 8)


# In[13]:


# Solve for Part 2
result_2 = execute_program_two(input_lines, 5)

