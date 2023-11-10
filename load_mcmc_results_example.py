#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arviz as az


# In[3]:


idata1 = az.from_netcdf("idata1.nc")
idata1


# In[6]:


idata1.posterior["d"].mean(("chain", "draw")).to_dataframe()


# In[8]:


idata1.posterior["e"].mean(("chain", "draw")).to_dataframe()


# In[ ]:




