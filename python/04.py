#!/usr/bin/env python
# coding: utf-8

# In[1]:


PUZZLE_INPUT = '124075-580769'


# ## Part 1

# In[2]:


start_range, end_range = [int(item) for item in PUZZLE_INPUT.split("-")]


# In[3]:


possibilities = [str(num) for num in range(start_range, end_range + 1)]


# In[4]:


# Filter for "two adjacent digits"
adjacent_digits = [num for num in possibilities if len(
    [True for selector in [str(i)*2 for i in range(0, 9+1)] if selector in num]) > 0]


# In[5]:


# Filter for "never decreasing digits"
def decrease_filter(str_num):
    prior = int(str_num[0])
    for n in str_num[1:]:
        if int(n) < prior:
            return False
        prior = int(n)
    return True


# In[6]:


no_decreased = [num for num in adjacent_digits if decrease_filter(num)]


# In[7]:


# Part 1 result
len(no_decreased)


# ## Part 2

# In[8]:


no_decreased_2 = [num for num in possibilities if decrease_filter(num)]


# In[9]:


def doubles_filter(str_num):
    for i in range(0, 9+1):
        if str(i) * 2 in str_num and str(i) * 3 not in str_num:
            return True
    return False


# In[10]:


adjacent_digits_2 = [num for num in no_decreased_2 if doubles_filter(num)]


# In[11]:


# Part 2 result
len(adjacent_digits_2)

