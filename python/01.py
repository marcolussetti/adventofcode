#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
from functools import reduce


# In[4]:


with open('../inputs/01', 'r') as f:
    lines = f.readlines()
lines = [int(line.strip()) for line in lines]


# ## Part One

# In[5]:


def calc_fuel(line):
    val = math.floor(line/3.0) - 2
    return val if val > 0 else 0


# In[6]:


fuels = list(map(calc_fuel, lines))


# In[5]:


result_part_1 = reduce(lambda acc, val: acc + val, fuels)
result_part_1


# ## Part Two

# In[6]:


def calc_fuel_with_fuel(line):
    module_fuel = calc_fuel(line)
    total_fuel = module_fuel
    residual_fuel = module_fuel
    while residual_fuel > 0:
        residual_fuel = calc_fuel(residual_fuel)
        total_fuel += residual_fuel
    return total_fuel


# In[7]:


fuels_two = list(map(calc_fuel_with_fuel, lines))
result_part_2 = reduce(lambda acc, val: acc + val, fuels_two)
result_part_2

