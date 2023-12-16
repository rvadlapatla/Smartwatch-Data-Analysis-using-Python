#!/usr/bin/env python
# coding: utf-8

# # Smartwatch Data Analysis using Python
# There is a lot of competition among the brands in the smartwatch industry. Smartwatches are preferred by people who like to take care of their fitness. Analyzing the data collected on your fitness is one of the use cases of Data Science in healthcare. So if you want to learn how to analyze smartwatch fitness data,

# Now I will start the task of Smartwatch Data Analysis by importing the necessary Python libraries and the datase

# In[ ]:





# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

data =pd.read_csv(r'C:\Users\User\Downloads\archive (7)\Fitabase Data 4.12.16-5.12.16\dailyActivity_merged.csv')
print(data.head())


# In[4]:


# finding null
print(data.isnull().sum())


# In[5]:


# collecting all info on data set
print(data.info())


# In[6]:


#cal all mean,std,count
print(data.describe())


# In[8]:


data["ActivityDate"]=pd.to_datetime(data["ActivityDate"],format ="%m/%d/%Y")
print(data.info())


# In[13]:


data["TotalMinutes"] =data["VeryActiveMinutes"] + data["FairlyActiveMinutes"] + data["LightlyActiveMinutes"] +data["SedentaryMinutes"]
print(data["TotalMinutes"].sample(10))


# In[14]:


print(data.describe())


# # Let’s Analyze the Smartwatch Data⌚️
# The dataset has a “Calories” column; it contains the data about the number of calories burned in a day. Let’s have a look at the relationship between calories burned and the total steps walked in a day:

# In[16]:


fig =px.scatter(data,x="Calories",y="TotalSteps",title =" Relation betwwen of cal and step",trendline ="ols",
                   size ="VeryActiveMinutes")
fig.show()


# You can see that there is a linear relationship between the total number of steps and the number of calories burned in a day. Now let’s look at the average total number of active minutes in a day

# In[22]:


label =["Very Active Minutes", "Fairly Active Minutes", 
         "Lightly Active Minutes", "Inactive Minutes"]
counts =data[["VeryActiveMinutes", "FairlyActiveMinutes", 
               "LightlyActiveMinutes", "SedentaryMinutes"]]
colors =['gold','lightgreen',"pink",'blue']
fig =go.Figure(data=[go.Pie(labels=label,values =counts.iloc[0])])
fig.update_layout(title_text="Total Active Minutes")
fig.update_traces(hoverinfo ='label+percent',textinfo ='value',textfont_size =30,
                marker =dict(colors =colors,line =dict(color ='black',width =3)))
fig.show()
                  
                  


# In[20]:


data["Day"] =data["ActivityDate"].dt.day_name()
print(data["Day"].head())


# In[ ]:





# In[24]:


#Now let’s have a look at the very active, fairly active, and lightly active minutes on each day of the week
fig.add_trace(go.Bar(x=data["Day"],y=data['VeryActiveMinutes'],name='Very Active',marker_color ="purple"))
fig.add_trace(go.Bar(x=data["Day"],y=data['FairlyActiveMinutes'],name='Fairly Active',marker_color ="green"))
fig.add_trace(go.Bar(x=data["Day"],y=data['LightlyActiveMinutes'],name='Lightly Active',marker_color ="pink"))
fig.update_layout(barmode ="group",xaxis_tickangle =-45)
fig.show()


# In[25]:


day = data["Day"].value_counts()
label = day.index
counts = data["SedentaryMinutes"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Inactive Minutes Daily')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# So Thursday is the most inactive day according to the lifestyle of all the individuals in the dataset. Now let’s have a look at the number of calories burned on each day of the week:

# In[26]:


calories = data["Day"].value_counts()
label = calories.index
counts = data["Calories"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Calories Burned Daily')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[ ]:




