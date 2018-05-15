from flask import Flask, render_template, request, json
import pandas as pd
import math
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('people.html')


@app.route("/profile/<name>")
def profile(name):
    person = filteredVCdata[filteredVCdata['Full Name'].str.startswith(name.lower())]
    print(person)
    return render_template('linked_profile.html', name=person['Full Name'].iloc[0].title(),
                           job=person['Primary Job Title'].iloc[0].title(),
                           company=person['Primary Company'].iloc[0].title(),
                           location=person['Location'].iloc[0].title(),
                           sector=person['Investment interest/sector'].iloc[0].title(),
                           stage=person['Stage (Pre-Seed, Seed, Series A/B/C)'].iloc[0].title(),
                           bio=person['Bio'].iloc[0],
                           picture=person['Row for Picture'].iloc[0])

# coding: utf-8

# In[1]:

import seaborn as sns
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from IPython.display import display, Latex, Markdown, HTML, Javascript

# In[90]:
rawAngelData = pd.read_csv('AngelData.csv', dtype=str)
rawPartnerData = pd.read_csv('PartnerData.csv', dtype=str)
rawFounderData = pd.read_csv('FounderData.csv', dtype=str)
#rawAssociateData = pd.read_excel(blnDataPath, 'Associates', dtype=str)
#rawvcData = pd.read_csv('blnData.csv', dtype=str)
#rawvcData.head()

rawAngelData.head()
rawPartnerData.head()
rawFounderData.head()

# In[ ]:

#Create Filtered Angel Data
filteredAngelData = rawAngelData.loc[:, ["Full Name", "Primary Job Title", "Primary Company", "Location",
                                   "Investment interest/sector", "Stage (Pre-Seed, Seed, Series A/B/C)", "Bio", "Row for Picture"]]
filteredAngelData["Row for Picture"] = "TypeA" + filteredAngelData["Row for Picture"] 
filteredAngelData.head()

#Create Filtered Partner Data
filteredPartnerData = rawPartnerData.loc[:, ["Full Name", "Primary Job Title", "Primary Company", "Location",
                                   "Investment interest/sector", "Stage (Pre-Seed, Seed, Series A/B/C)", "Bio", "Row for Picture"]]
filteredPartnerData["Row for Picture"] = "TypeP" + filteredPartnerData["Row for Picture"] 
filteredPartnerData.head()


#Create Filtered Founder Data
filteredFounderData = rawFounderData.loc[:, ["Full Name", "Primary Job Title", "Primary Company", "Location",
                                   "Investment interest/sector", "Stage (Pre-Seed, Seed, Series A/B/C)", "Bio", "Row for Picture"]]
filteredFounderData["Row for Picture"] = "TypeF" + filteredFounderData["Row for Picture"] 
filteredFounderData.head()




frames = [filteredAngelData, filteredPartnerData, filteredFounderData]
filteredVCdata = pd.concat(frames) 


# # In[91]:

# rawvcData.columns

# # In[92]:

# filteredVCdata = rawvcData.loc[:, ["Full Name", "Primary Job Title", "Primary Company", "Location",
#                                    "Investment interest/sector", "Stage (Pre-Seed, Seed, Series A/B/C)", "Bio", "Row for Picture"]]

# # In[93]:

filteredVCdata.head()

# Angel/ partner/ founder
# location -- DONE
# Actively investing -- DONE
# Sector --- DONE

# In[ ]:




# In[94]:

for x in filteredVCdata.columns:
    if(x != "Bio" and x != "Row for Picture"):
        filteredVCdata[x] = filteredVCdata[x].str.lower()
    if(x == "Row for Picture"):
        filteredVCdata[x] = filteredVCdata[x].str.replace('/','')
        filteredVCdata[x] = filteredVCdata[x].str.replace('@','')
        filteredVCdata[x] = filteredVCdata[x].str.replace("TypeA","/static/images/Pictures_Angels/")
        filteredVCdata[x] = filteredVCdata[x].str.replace("TypeP","/static/images/Pictures_Partners/")
        filteredVCdata[x] = filteredVCdata[x].str.replace("TypeF","/static/images/Pictures_Founders/")

        
# In[95]:

filteredVCdata.fillna('Null', inplace=True)


# In[96]:

#Returns if indicated investor contains the investment stage searched
def stageFilter(stageName):
    
    stageNameLowered = stageName.lower()
    return filteredVCdata[filteredVCdata["Stage (Pre-Seed, Seed, Series A/B/C)"].str.contains(stageNameLowered) == True]

# All results for the corresponding industry sector
def sectorFilter(sectorName):
    sectorNamelowered = sectorName.lower()
    return filteredVCdata[filteredVCdata["Sector "].str.contains(sectorNamelowered) == True]


# In[97]:

# sectorFilter("software")


# In[98]:

# Returns if the indicated investor is actively investing or not
def activeInvestor(firstName, lastName):
    nameNoSpace = filteredVCdata
    nameNoSpace["Full Name"] = nameNoSpace["Full Name"].str.replace(" ", "")
    fnLower = firstName.lower()
    lnLower = lastName.lower()
    fullName = fnLower + lnLower
    isolatedInvestor = nameNoSpace[nameNoSpace["Full Name"].str.contains(fullName) == True]

    return isolatedInvestor["Actively investing?"]


# In[99]:

# activeInvestor("benjamin", "ling")


# In[100]:

# Returns the location of the given investor
def locateInvestor(firstName, lastName):
    nameNoSpace = filteredVCdata
    nameNoSpace["Full Name"] = nameNoSpace["Full Name"].str.replace(" ", "")
    fnLower = firstName.lower()
    lnLower = lastName.lower()
    fullName = fnLower + lnLower
    isolatedInvestor = nameNoSpace[nameNoSpace["Full Name"].str.contains(fullName) == True]

    return isolatedInvestor["Location"]


# In[101]:

# locateInvestor("benjamin", "ling")


# In[114]:

# Returns those with the given job title
def roleFilter(jobTitle):
    nameNoSpace = filteredVCdata
    nameNoSpace["Primary Job Title"] = nameNoSpace["Primary Job Title"].str.replace(" ", "")
    jobTitleLower = jobTitle.lower()
    investorJob = nameNoSpace[nameNoSpace["Primary Job Title"].str.contains(jobTitleLower) == True]

    #     s1 = pd.merge(filteredVCdata, investorJob, how='inner', on=["Full Name"])
    #     s1.dropna(inplace = True)
    return investorJob


    # In[116]:

    # roleFilter("founder").head()


    # In[ ]:




    # In[ ]:

person = None

@app.route("/dataRequest", methods=['POST'])
def dataRequest():
    return json.dumps(filteredVCdata.to_dict('list'))


if __name__ == "__main__":
    app.run(port=9077)

