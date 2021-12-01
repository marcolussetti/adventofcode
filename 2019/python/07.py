#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools


# In[2]:


with open('../inputs/07', 'r') as f:
    file_lines = f.readlines()
input_lines = [int(line.strip()) for line in file_lines[0].split(",")]


# ## Part 1

# In[3]:


def execute_program(program, inputs):
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
            p[p[i+1]] = inputs.pop(0) if len(inputs) > 0 else inputs[0]
            i += 2
        elif op == 4:  # Output
            return(p[p[i+1]])
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


# In[4]:


execute_program([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4,0])


# In[5]:


def chain_programs(program, phases):
    output = 0
    for i, phase in enumerate(phases):
        output = execute_program(program, [phase, output])
        
    return output


# In[6]:


chain_programs([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], [9,8,7,6,5])


# In[7]:


phases_permutations = list(itertools.permutations([0,1,2,3,4], 5))


# In[8]:


phases_permutations_results = {permutation: chain_programs(input_lines, permutation)
                               for permutation in phases_permutations}


# In[9]:


[(k, v) for k, v in phases_permutations_results.items()
 if v == max(phases_permutations_results.values())]


# ## Part 2

# In[10]:


def execute_program_two(program, inputs, i=0):
    p = program.copy()
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
            p[p[i+1]] = inputs.pop(0) if len(inputs) > 0 else inputs[0]
            i += 2
        elif op == 4:  # Output
            return [i + 2, p.copy(), p[p[i+1]]]
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

    return [-1, None, None]


# In[11]:


def chain_programs_loop(program, phases):
    amps = [program.copy(), program.copy(), program.copy(),
            program.copy(), program.copy()]
    amps_i = [0, 0, 0, 0, 0]
    amps_active = list(range(0, 5))
    output = 0
    result = None
    while len(amps_active) > 0:
        for amp in amps_active:
            program = amps[amp].copy()
            i = amps_i[amp]
            phase = phases[amp]
            program_input = [phase, output] if i == 0 else [output]
            amp_i, amp_p, output = execute_program_two(
                program, program_input, i)
#             print(output)
            if output is not None:
                result = output
            if amp_i == -1:
                amps_active.remove(amp)
            else:
                amps[amp] = amp_p.copy()
                amps_i[amp] = amp_i

    return result


# In[12]:


chain_programs_loop([3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
                     27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5], [9, 8, 7, 6, 5])


# In[13]:


phases_permutations_two = list(itertools.permutations([9,8,7,6,5], 5))


# In[14]:


phases_permutations_results_two = {permutation: chain_programs_loop(input_lines, permutation)
                                   for permutation in phases_permutations_two}


# In[15]:


[(k, v) for k, v in phases_permutations_results_two.items()
 if v == max(phases_permutations_results_two.values())]

