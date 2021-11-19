#!/usr/bin/env python
# coding: utf-8

# In[5]:


def is_divisible_by_k(x,k):
    '''
    Checks whether x is divisible by k.
    '''
    if x%k == 0:
        return True


# In[9]:


'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''
x = []
for i in range(1001):
    if is_divisible_by_k(i,2) == True or is_divisible_by_k(i,5) == True or is_divisible_by_k(i,7) == True:
        x.append(i)
print(x)


# In[8]:


'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''
sum(x)


# In[ ]:




