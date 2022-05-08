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
st.write('You selected:', country_selected)

pd.read_sql("SELECT participants.country, shortName, name, activityType, ecContribution, organizationURL, role, countries.Country FROM Participants LEFT JOIN countries ON participants.country=countries.Acronym", conn)
c1=pd.read_sql("SELECT country, shortName, name, activityType, ecContribution, organizationURL FROM Participants WHERE role = 'coordinator' AND Country=st.write('You selected:', country_selected)",conn)
df_participants = pd.DataFrame(c1, columns= ['country', 'shortName', 'name', 'activityType', 'Sum','organizationURL', 'count'])
st.dataframe(df_participants)
