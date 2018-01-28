import pandas as pd
import os

#saving a processed file
def save(file):
    file.to_csv("updated_OLYMPICS.csv", encoding='utf-8')

#loading a preprocessed file
def load(file):
    return (pd.read_csv(file, sep=','))
    
#return all information regarding first country
def first_function(dataframe):
    return dataframe.head(1)

#country which is having max number gold medals in summer
def medal(dataframe,season,medal_name):
    return(dataframe.loc[dataframe[medal_name].idxmax()])

#maximum difference between summer's gold and winter's gold medals
def max_diff(dataframe):
    dataframe["difference"] = dataframe["Gold"]-dataframe["Gold.1"]
    x = (dataframe.loc[dataframe["difference"].idxmax()])
    dataframe = dataframe.drop("difference",axis=1)
    return x

#calculating points
def points(dataframe):
    dataframe['points'] = (3*dataframe['Gold.2']) + (2*dataframe['Silver.2']) + dataframe['Bronze.2']
    return dataframe
  
data3 = load("updated_OLYMPICS.csv")
data3.set_index("Country")
data3 = data3.drop("Unnamed: 0",axis=1)
data3 = data3.drop(data3.index[-1])

first = first_function(data3)
print(first)

gold = medal(data3,"summer","Gold")
print(gold)

diff = max_diff(data3)
print(diff)

data3 = points(data3)
data3.head()
