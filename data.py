import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def getData():

    path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/02-05-2022.csv'

    df = pd.read_csv(path)

    df.info()

    df.drop(['FIPS', 'Admin2','Last_Update','Province_State', 'Combined_Key'], axis=1, inplace=True)

    df.rename(columns={'Country_Region': "Country"}, inplace=True)

    world = df.groupby("Country")['Confirmed','Active','Recovered','Deaths','Incident_Rate'].mean().reset_index()

    ### Find top 20 countries with maximum number of confirmed cases
    # 
    top = world.sort_values(by=['Confirmed'],
    ascending=False).head()

    maxVal = 0

    for i,(value,name) in enumerate(zip(top['Confirmed'],top['Country'])):    
        top['Active'] = value**(1/3)
        if top['Active'] >= maxVal:
            maxVal = top['Active']

    for i,(value,name) in enumerate(zip(top['Active'],top['Country'])):    
        top['Active'] = (top['Active']/maxVal)*100

    risk = top.sort_values(by=['Active'],
    ascending=False).head()

    return risk

    # for country do risk['Country']
    # for risk level normalized between 0 and 100 do risk['Active']
