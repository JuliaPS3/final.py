import sqlite3
import pandas as pd
from sqlite3 import connect

conn = sqlite3.connect('db1.db')
cur = conn.cursor()
cur.execute('SELECT Country, Acronym FROM Countries')
df = pd.DataFrame(cur.fetchall(), columns = ['Countries', 'Acronym'])


import streamlit as st
import pandas as pd
countries_column = df['Countries']
countries = []
for i in countries_column:
  countries.append(i)
country_selected = st.selectbox('Country name', countries)

for i in range(len(countries)):
  if countries[i]==country_selected:
    position=i
  
acronym_column = df['Acronym']
acronym=[]
for i in acronym_column:
  acronym.append(i)
my_acronym=acronym[position]


st.write('You selected:', country_selected,',',my_acronym)




c1=pd.read_sql("SELECT country, shortName, name, activityType, SUM(ecContribution), organizationURL, COUNT(organizationURL) FROM participants WHERE country=='FR' GROUP BY organizationURL ORDER BY SUM(ecContribution)".format(country_selected),conn)
df_participants = pd.DataFrame(c1, columns= ['country', 'shortName', 'name', 'activityType', 'Sum','organizationURL', 'count'])  
st.dataframe(df_participants)
