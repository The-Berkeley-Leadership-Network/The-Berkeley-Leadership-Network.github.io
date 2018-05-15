
# coding: utf-8

# In[1]:

import seaborn as sns
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
sns.set()
sns.set_context("talk")

from IPython.display import display, Latex, Markdown, HTML, Javascript


# In[90]:

rawvcData = pd.read_csv('blnData.csv')
rawvcData.head()


# In[ ]:




# In[91]:

rawvcData.columns


# In[92]:

filteredVCdata = rawvcData.loc[:, ["Full Name", "Primary Job Title", "Primary Company", "Location",
                                   "Investment interest/sector", "Stage (Pre-Seed, Seed, Series A/B/C)"]]

# In[93]:

filteredVCdata.head()


# Angel/ partner/ founder
# location -- DONE
# Actively investing -- DONE
# Sector --- DONE

# In[ ]:




# In[94]:

for i in range(len(filteredVCdata.columns)):
    for x in filteredVCdata.columns:
        filteredVCdata[x] = filteredVCdata[x].str.lower()


# In[95]:

filteredVCdata.head()


# In[96]:

#Returns if indicated investor contains the investment stage searched
def stageFilter(stageName):
    
    stageNameLowered = stageName.lower()
    return filteredVCdata[filteredVCdata["Stage (Pre-Seed, Seed, Series A/B/C)"].str.contains(stageNameLowered) == True]

#All results for the corresponding industry sector
def sectorFilter(sectorName):
    
    sectorNamelowered = sectorName.lower()
    return filteredVCdata[filteredVCdata["Sector "].str.contains(sectorNamelowered) == True]


# In[97]:

#sectorFilter("software")


# In[98]:

#Returns if the indicated investor is actively investing or not
def activeInvestor(firstName, lastName):
    
    nameNoSpace = filteredVCdata
    nameNoSpace["Full Name"] = nameNoSpace["Full Name"].str.replace(" ", "")
    fnLower = firstName.lower()
    lnLower = lastName.lower()
    fullName = fnLower+lnLower
    isolatedInvestor = nameNoSpace[nameNoSpace["Full Name"].str.contains(fullName) == True]
        
    return isolatedInvestor["Actively investing?"]


# In[99]:

#activeInvestor("benjamin", "ling")


# In[100]:

#Returns the location of the given investor
def locateInvestor(firstName, lastName):
    
    nameNoSpace = filteredVCdata
    nameNoSpace["Full Name"] = nameNoSpace["Full Name"].str.replace(" ", "")
    fnLower = firstName.lower()
    lnLower = lastName.lower()
    fullName = fnLower+lnLower
    isolatedInvestor = nameNoSpace[nameNoSpace["Full Name"].str.contains(fullName) == True]
        
    return isolatedInvestor["Location"]


# In[101]:

#locateInvestor("benjamin", "ling")


# In[114]:

#Returns those with the given job title
def roleFilter(jobTitle):
    
    nameNoSpace = filteredVCdata
    nameNoSpace["Primary Job Title"] = nameNoSpace["Primary Job Title"].str.replace(" ", "")
    jobTitleLower = jobTitle.lower()
    investorJob = nameNoSpace[nameNoSpace["Primary Job Title"].str.contains(jobTitleLower) == True]
        
#     s1 = pd.merge(filteredVCdata, investorJob, how='inner', on=["Full Name"])
#     s1.dropna(inplace = True)
    return investorJob


# In[116]:

#roleFilter("founder").head()


# In[ ]:




# In[ ]:



