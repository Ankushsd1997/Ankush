#!/usr/bin/env python
# coding: utf-8

# # NAME:ANKUSH SHIVAJIRAO DHUMALE
# (BEGINNER LEVEL)

# # TASK 1ST:PREDICTION OF SCORE BASED ON NUMBER OF STUDY HOURS
# 

# PROBLEM STATEMENT:
# PREDICT THE PERCENTAGE OF STUDENT  BASED ON THE NUMBER OF STUDY HOURS

# IMPORTING THE NECESSARY LIBRARIES

# In[1]:


#importing necessary libraries
import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# libraries imported sucessfully

# the given file is in csv format
# reading the data in pandas

# In[2]:


#reading the dataset using pandas 
link='http://bit.ly/w-data'
df=pd.read_csv(link)
df.head()


# data read sucessfully in pandas and stored it in 'df' variable

# In[3]:


#cheking shape of given data
df.shape


# there are about 25 rows and 2 columns this is pretty simple example

# now chek is their any missing value in data set if yes we replace it by some appropriate value

# In[4]:


df.isnull().sum()


# from above its cleared that there is no null value in the data set

# to chek whther any outlier in the data set

# In[32]:


df['Hours'].plot.box()


# hence from above it clear that there no outlier in the data set of hours

# now  chek same for scores

# In[33]:


df['Scores'].plot.box()


# hence also the scores does not have any outliers,this pretty clean dataset

# to chek correlation among the data set

# In[35]:


df.corr()


# from above its cleared that there is strong corelation btween the hours and scores

# # ploting the graphs to chek relation between the hours and scores

# now cheking the relation between the hours and scores by ploting the graph

# In[26]:


df.plot(x='Hours',y='Scores',style='o')
plt.title('HOURS VS SCORES')
plt.xlabel('Hours studied')
plt.ylabel('percentage Scored')
plt.show()


# from above graph its cleared that there is linear relationship between student scores and study hours

# # seprating the data as train and test data

# now seprate the data from "df" as train and test

# In[6]:


train=df[0:16]
test=df[16:26]


# In[7]:


#let's chek the shape of train and test data set
train.shape


# In[8]:


test.shape


# hence we seprated data as train and test for training our model

# now seprate  data  for training on x and y axis to train hours on x- axis we drop the scores data from training data.

# In[9]:


x_train=train.drop('Scores',axis=1)
x_train


# hence x_train now  contain hours of study only

# now train the data for y axis generally on y-axis we plot dependent variable in this case its scores which we have to predict later

# In[10]:


y_train=train['Scores']
y_train


# y_train contain scores that is our dependent variable

# now also from test drop scores which we store in next step as true prediction to chek with model prediction

# In[11]:


x_test=test.drop('Scores',axis=1)
x_test


# In[12]:


#true predication
y_test=test['Scores']


# # training the algorithm

# from scikit learn library impoting linearregression model to train our data

# In[13]:


from sklearn.linear_model import LinearRegression


# sucessfully imported linear regression

# training the our data

# In[14]:


lreg=LinearRegression()
lreg.fit(x_train,y_train)


# # predication

# our model  now ready to predict values lets chek for our test data

# In[15]:


pred=lreg.predict(x_test)
pred


# now our y_test that is actual values

# In[16]:


y_test


# arrange both true value and  predicted value in columns to betterr understand how accuratly our model predict

# In[17]:


dataframe=pd.DataFrame({'Actual':y_test,'predicted':pred})
dataframe


# In[18]:


lreg.score(x_test,y_test)


# In[19]:


lreg.score(x_train,y_train)


# hence from above score is closely releted our training is done well

# # to chek for 9.25 hours

# now to predict the marks for 9.25 hours of study

# In[20]:


new_output=lreg.predict([[9.25]])


# In[21]:


new_output


# #                        THANK YOU!
# 
# 
# 
# 
# 
