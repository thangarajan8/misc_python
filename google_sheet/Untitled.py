#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np
from pathlib import Path
from string import ascii_letters

df = pd.DataFrame(np.random.randint(0,10000,size=(1000000, 52)),columns=list(ascii_letters))
df.to_csv('csv_store.csv',index=False)
print('CSV Consumend {} MB'.format(Path('csv_store.csv').stat().st_size*0.000001))
df.to_parquet('parquate_store',index=False)
print('Parquet Consumed {} MB'.format(Path('parquate_store').stat().st_size*0.000001))


# In[ ]:




