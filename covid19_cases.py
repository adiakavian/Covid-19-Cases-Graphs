# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 18:59:54 2022

@author: Adi Akavian
"""

import matplotlib.pyplot as plt
import pandas as pd

#load the covid-19 data into a Pandas’ dataframe (the data updates automatically every day. 
web = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
df=pd.read_csv(web)

#Generate a new dataframe that contains the data from the specific countries.
lst=['Canada', 'Germany', 'United Kingdom', 'US', 'France','China', 'India']
new_data=df[df.Country.isin(lst)]

"""
Add a summary column that sums the total number of cases across the
confirmed cases, recovered cases, and any individuals who have died
as a result of COVID-19. 
"""
new_data['Total']=new_data.loc[:,'Confirmed']+new_data.loc[:,'Recovered']+new_data.loc[:,'Deaths']

#Plot the number of total cases over time in 2021 in the countries from the previous section
data_2021 = new_data.copy()
data_2021['Date']=pd.to_datetime(data_2021.Date,format='%Y-%m-%d')
data_2021['Year']=data_2021.Date.dt.year
data_2021=data_2021[data_2021.loc[:,'Year']==2021]

plt.figure('The number of total cases over time',figsize = (10,8),dpi=120)
country_group = data_2021.groupby('Country')
for name,group in country_group:
    C_df=country_group.get_group('{}'.format(name))
    plt.plot(C_df.Date,C_df.Total,label='{}'.format(name)) 
    plt.text(C_df.loc[C_df.index[(len(C_df['Date'])-1)],'Date'],C_df.loc[C_df.index[(len(C_df['Date'])-1)],'Total'],'{}'.format(name),fontsize=7,color='k',fontweight='bold')

plt.suptitle("Covid-19 Cases by Country",fontsize=16,fontweight='bold',color = 'navy')
plt.xlabel('Date',fontsize=10,fontweight='bold')
plt.ylabel('Number of Cases',fontsize=10,fontweight='bold')
plt.grid()
plt.legend()