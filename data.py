import pandas as pd

def getData():

    path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/02-05-2022.csv'

    df = pd.read_csv(path)

    print(len(df))

    df.info()

    df.drop(['FIPS', 'Admin2','Last_Update','Province_State', 'Combined_Key'], axis=1, inplace=True)

    df.rename(columns={'Country_Region': "Country"}, inplace=True)

    world = df.groupby("Country")['Confirmed','Active'].mean().reset_index()

    ### Find top 20 countries with maximum number of confirmed cases
    # 
    top = world

    print(len(top))

    risk = []

    maxVal = 0
    n = 0

    for i,(value,name) in enumerate(zip(top['Confirmed'],top['Country'])):    
        risk = risk + [[value**(1/3), name]]
        n += 1
        if value**(1/3) > maxVal:
            maxVal = value**(1/3)

        
    for i in range(len(risk)):    
        risk[i] = [(risk[i][0]/maxVal)*100, risk[i][1]]
        n += 1
    
    print(n)

    return risk

    # for country do risk[i][1]
    # for risk level do risk[i][0]