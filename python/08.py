#!/usr/bin/env python
# coding: utf-8

# In[6]:


with open('../inputs/08', 'r') as f:
    input_string = f.readlines()[0].strip()


# ## Part 1

# In[131]:


layers = []
i = 0
while i < len(input_string):
    layers.append(input_string[i:i+25*6])
    i += 25*6


# In[132]:


layers_int = [[int(char) for char in layer] for layer in layers]


# In[136]:


layers_count_zeros = [sum([1 for char in layer if char == 0]) for layer in layers_digits]
layer_less_zeros = [i for i, zeros in enumerate(layers_count_zeros) if zeros == min(layers_count_zeros)][0]
print(f"Layer {layer_less_zeros}: {layers_count_zeros[layer_less_zeros]}")


# In[137]:


sum([1 for char in layers_digits[layer_less_zeros] if char == 1]) *     sum([1 for char in layers_digits[layer_less_zeros] if char == 2])


# ## Part 2

# In[139]:


def find_topmost_pixel(pixel_array):
    for item in pixel_array:
        if item == 0 or item == 1:
            return item
#     return 9


# In[140]:


layers_test = [[0,2,2,2], [1,1,2,2], [2,2,1,2], [0,0,0,0]]


# In[152]:


def image_from_layers(layers):
    pixel_groups = list(zip(*layers))
    image_array = [find_topmost_pixel(pixel_group) for pixel_group in pixel_groups]
    
    return image_array


# In[154]:


"".join([str(item) for item in image_from_layers(layers_test)])


# In[164]:


# Result
image_as_numbers = image_from_layers(layers_int)
"".join([str(item) for item in image_from_layers(layers_int)])


# In[167]:


def print_image(image_array, width, ascii=False):
    ascii_map = ["█", "░"]
    for i, item in enumerate(image_array):
        if i > 0 and i % width == 0:
            print()
        print(f"{str(item) if not ascii else ascii_map[item]}", end = '')


# In[168]:


print_image(image_as_numbers,25)


# In[169]:


print_image(image_as_numbers,25,ascii=True)

