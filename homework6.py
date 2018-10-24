#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np
from IPython import __version__ as ipython_version
from pandas import __version__ as pandas_version
from bokeh import __version__ as bokeh_version
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import GnBu3, OrRd3
from bokeh.palettes import Viridis10
from bokeh.palettes import Plasma10
from bokeh.palettes import Category20c
import matplotlib.pyplot as plt


# In[65]:


output_notebook()


# In[66]:


data = pd.read_csv('F:\\UIUC\\590DV\\homework6\\2007_2017_members.csv')


# ### Because we are trying to investigate the country's government corruption situation, there is no urgent need to look into data that are ages ago. Thus, I choose the most recent 10 years from 2007 to 2017 to get a glimpse of what is happening in the U.S. Senate election.  
# ### This homework will focus on the following 2 questions:
# ### 1. How were those candidate elected ?
# ### 2. What percentage were each party members selected during 2007 to 2017?

# ### 1. How were those candidate elected ?
# Based on what is explained in the data dictionary of the election data, I choose variable 'last means' to see in the 10 year-period how the candidated were elected by calculating how much of each way in all four electing ways using a bar chart.

# In[73]:


data['last_means'] = data['last_means'].astype(int)
count1 = 0
count2 = 0
count3 = 0
count5 = 0
countall = 0
for index,row in data.iterrows():
    countall = countall +1
    if row['last_means'] == 1:
        count1 = count1+1
    elif row['last_means'] == 2:
        count2 = count2+1
    elif row['last_means'] == 3:
        count3 = count3+1
    else:
        count5 = count5+1


# In[74]:


counta = ['general election','special election','state legislature','appointed']
p1 = figure(x_range = counta, plot_height = 250, title = 'Ways of Selecting Senators by Number')
p1.vbar(x=counta,top = [count1,count2,count3,count5],width = 0.7)
p1.xgrid.grid_line_color = None
p1.y_range.start = 0
show(p1)


# In[75]:


p2 = figure(x_range = counta, plot_height = 250, title = 'Ways of Selecting Senators by Percentage')
p2.vbar(x=counta,top = [count1/countall,count2/countall,count3/countall,count5/countall],width = 0.7)
p2.xgrid.grid_line_color = None
p2.y_range.start = 0
show(p2)


# From the graphs above, we can see that almost 95% cancidates were selected by general election. Thus, there are very few people who had 'special treatment'.

# ### 2. What percentage were each party members during 2007 to 2017?
# The answer to this question will allow us to know the change of constitution of House of Senate. To see if there was a period when one party was dominat the 'upper' house.
# To answer this question, I choose variable 'congress' and 'party_code'.

# In[76]:


data['party_code'] = data['party_code'].astype(int)
data['congress'] = data['congress'].astype(int)
countd0 = 0
countr0 = 0
counto0 = 0
count0 = 0
for index,row in data.iterrows():
    count0 = count0+1
    if row['congress']==110:
        if row['party_code'] == 100:
            countd0 = countd0+1
        elif row['party_code'] == 200:
            countr0 = countr0+1
        else:
            counto0 = counto0+1

countd1 = 0
countr1 = 0
counto1 = 0
count1 = 0
for index,row in data.iterrows():
    count1 = count1+1
    if row['congress']==111:
        if row['party_code'] == 100:
            countd1 = countd1+1
        elif row['party_code'] == 200:
            countr1 = countr1+1
        else:
            counto1 = counto1+1

countd2 = 0
countr2 = 0
counto2 = 0
count2 = 0
for index,row in data.iterrows():
    count2 = count2+1
    if row['congress']==112:
        if row['party_code'] == 100:
            countd2 = countd2+1
        elif row['party_code'] == 200:
            countr2 = countr2+1
        else:
            counto2 = counto2+1
            
countd3 = 0
countr3 = 0
counto3 = 0
count3 = 0
for index,row in data.iterrows():
    count3 = count3+1
    if row['congress']==113:
        if row['party_code'] == 100:
            countd3 = countd3+1
        elif row['party_code'] == 200:
            countr3 = countr3+1
        else:
            counto3 = counto3+1
            
countd4 = 0
countr4 = 0
counto4 = 0
count4 = 0
for index,row in data.iterrows():
    count4 = count4+1
    if row['congress']==114:
        if row['party_code'] == 100:
            countd4 = countd4+1
        elif row['party_code'] == 200:
            countr4 = countr4+1
        else:
            counto4 = counto4+1
            
countal = count0+count1+count2+count3+count4


# In[87]:


Years = ['07-09','09-11','11-13','13-15','15-17']
d = [countd0/countal,countd1/countal,countd2/countal,countd3/countal,count4/countal]
r = [countr0/countal,countr1/countal,countr2/countal,countr3/countal,countr4/countal]
o = [counto0/countal,counto1/countal,counto2/countal,counto3/countal,counto4/countal]
p3 = figure(title = 'Percentage of Senate Party From 2007-2017',x_axis_label='Year',y_axis_label='Percentage',plot_width = 400,plot_height = 450)
p3.line(x = d,y= Years, legend = 'Democratic',line_color = 'tomato',line_width = 2)
p3.line(x = r,y= Years, legend = 'Republican',line_color = 'indigo',line_width = 2)
p3.line(x = o,y= Years, legend = 'Other Party',line_color = 'gold',line_width = 2)

show(p3)


# In[88]:


d


# In[89]:


r


# In[90]:


o


# I don't know why thr graph didn't show but from the data below we can see that the percentage from these five periods between democratic and repubilican are almost the same, while other party have very little people in Senate.
# Still, it is kind of odd that those percentages don't add up to 100%.

# In[ ]:




