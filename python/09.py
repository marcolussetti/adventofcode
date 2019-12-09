#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools


# In[2]:


with open('../inputs/09', 'r') as f:
    file_lines = f.readlines()
input_lines = [int(line.strip()) for line in file_lines[0].split(",")]


# ## Part 1

# In[3]:


def execute_program(program, inputs):
    p = program.copy()
    p.extend([0]*10000)
    i = 0
    relative_base = 0
    while p[i] != 99:
        # Extract operation
        op = int(str(p[i])[-2:])
        # Extract modes after zero filling it & inverting
        modes = [int(char) for char in str(p[i])[:-2].zfill(3)][::-1]

        # Map variables/locations based on operation
        if op in [1, 2, 7, 8]:
            # Two parameters, 1 target
            variables = [
                p[i+1] if modes[0] == 1 else p[p[i+1]+relative_base] if modes[0] == 2 else p[p[i+1]],
                p[i+2] if modes[1] == 1 else p[p[i+2]+relative_base] if modes[1] == 2 else p[p[i+2]],
                i+3 if modes[2] == 1 else p[i+3]+relative_base if modes[2] == 2 else p[i+3]
            ]
        elif op in [5, 6]:
            # Two parameters
            variables = [
                p[i+1] if modes[0] == 1 else p[p[i+1]] if modes[0] == 0 else p[p[i+1]+relative_base],
                p[i+2] if modes[1] == 1 else p[p[i+2]] if modes[1] == 0 else p[p[i+2]+relative_base],
            ]
        elif op in [3, 4]:
            # One location?
            variables = [
                i+1 if modes[0] == 1 else p[i+1] + relative_base if modes[0] == 2 else p[i+1]
            ]
        elif op in [9]:
            # One parameter
            variables = [
                p[i+1] if modes[0] == 1 else p[p[i+1]] if modes[0] == 0 else p[p[i+1]+relative_base],
            ]

        # Perform operation
        if op == 1:  # Sum
            p[variables[2]] = variables[0] + variables[1]
            i += 4
        elif op == 2:  # Multiplication
            p[variables[2]] = variables[0] * variables[1]
            i += 4
        elif op == 3:  # Input
            p[variables[0]] = inputs.pop(0) #  if len(inputs) > 0 else inputs[0]
            i += 2
        elif op == 4:  # Output
            print(p[variables[0]])
            i += 2
        elif op == 5:  # Jump-if-true
            i = variables[1] if variables[0] else i + 3
        elif op == 6:  # Jump-if-false
            i = i + 3 if variables[0] else variables[1]
        elif op == 7:  # Less-than
            p[variables[2]] = int(variables[0] < variables[1])
            i += 4
        elif op == 8:  # Equals
            p[variables[2]] = int(variables[0] == variables[1])
            i += 4
        elif op == 9:  # Relative base adjustment
            relative_base += variables[0]
            i += 2
        else:  # ERROR!!
            print("Oops...")

    return p


# In[4]:


a = execute_program([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99],[])


# In[5]:


a = execute_program([1102,34915192,34915192,7,4,7,99,0],[])


# In[6]:


a = execute_program([104,1125899906842624,99],[])


# In[7]:


# part 1 result
result_1 = execute_program(input_lines,[1])


# ## Part 2

# In[8]:


# part 2 result
result_2 = execute_program(input_lines,[2])

