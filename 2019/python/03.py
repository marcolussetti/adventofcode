#!/usr/bin/env python
# coding: utf-8

# ## Part 1

# In[1]:


with open('../inputs/03', 'r') as f:
    file_lines = f.readlines()
input_lines = [[item.strip() for item in line.split(",")]
               for line in file_lines]


# In[2]:


# input_lines


# In[3]:


test_inputs_1 = [
    "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","),
    "U62,R66,U55,R34,D71,R55,D58,R83".split(",")
]
test_inputs_2 = [
    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","),
    "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")
]


# In[4]:


def generate_points(instructions):
    current_point = [0, 0]
    points = []
    for instruction in instructions:
        direction = instruction[0]
        value = int(instruction[1:])
        for i in range(0, value):
            if direction == "R":
                current_point[1] += 1
            elif direction == "L":
                current_point[1] -= 1
            elif direction == "U":
                current_point[0] += 1
            elif direction == "D":
                current_point[0] -= 1
            points.append(tuple(current_point.copy()))
    return points


# In[5]:


def manhattan_distance(a, b):
    return sum([abs(x1 - x2) for x1, x2 in zip(a, b)])


# In[6]:


def common_elements(a, b):
    return set(a) & set(b)


# In[7]:


def compute_min_manhattan_distance(a, b):
    points_a = generate_points(a)
    points_b = generate_points(b)
    common_points = common_elements(points_a, points_b)
    distances = [manhattan_distance(point, [0, 0]) for point in common_points]

    return min(distances)


# In[8]:


compute_min_manhattan_distance(*test_inputs_1)


# In[9]:


compute_min_manhattan_distance(*test_inputs_2)


# In[10]:


# Result 1
compute_min_manhattan_distance(*input_lines)


# ## Part 2

# In[11]:


def step_distance(point, a, b):
    step_counter = 0
    for step in a:
        step_counter += 1
        if step == point:
            break
    for step in b:
        step_counter += 1
        if step == point:
            break
    return step_counter


# In[12]:


def compute_min_step_distance(a, b):
    points_a = generate_points(a)
    points_b = generate_points(b)
    common_points = common_elements(points_a, points_b)
    distances = [step_distance(point, points_a, points_b)
                 for point in common_points]

    return min(distances)


# In[13]:


compute_min_step_distance(*test_inputs_1)


# In[14]:


compute_min_step_distance(*test_inputs_2)


# In[15]:


# Result 2
compute_min_step_distance(*input_lines)

