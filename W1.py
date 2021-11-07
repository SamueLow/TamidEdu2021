#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import csv
import json


# In[25]:


data_file = json.load(open("Students.json"))
students = data_file["Students"]

new_file = open("students.csv", "w")
csv_writer = csv.writer(new_file)
csv_writer.writerow(students.keys())
for student in students:
    print (student)
    csv_writer.writerow(students[student].values())
new_file.close()


# In[26]:


df = pd.read_csv("students.csv")
df


# In[30]:


averages = df["0"]
print (averages)


# In[ ]:




