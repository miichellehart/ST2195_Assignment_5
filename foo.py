#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def is_divisible_by_k(x,k):
    '''
    Checks whether x is divisible by k.
    '''
    assert x%k == 0


# In[ ]:


'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''
x = ()
for i in range(1000):
    if(is_divisible_by_k(x,2) & is_divisible_by_k(x,3)) | is_divisible_by_k(x,7):
        x.append(i)


# In[ ]:


'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''
sum(x)

