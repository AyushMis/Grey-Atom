import pandas as pd
import os

def save(file):
    file.to_csv("updated_OLYMPICS.csv", encoding='utf-8', sep='\t') 
    
data  = pd.read_csv('olympics.csv', header=1)
data2 = data.drop([0],axis=0)
data2 = data2.rename(columns={"Unnamed: 0":"Country", "01 !": "Gold", "02 !": "Silver", "03 !":"Bronze", "01 !.1": "Gold", "02 !.1": "Silver", "03 !.1":"Bronze", "01 !.2": "Gold", "02 !.2": "Silver", "03 !.2":"Bronze"})
data2 = data2.drop(["Combined total","Total","Total.1"], axis=1)
data2.head(3)

data2['Country_code'] = data2.Country.str.split('(').str.get(1)
data2['Country'] = data2.Country.str.split('(').str.get(0)
data2.head(3)

save(data2)
