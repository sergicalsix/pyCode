#!/usr/bin/env python
# coding: utf-8
import pandas as pd
df_population = pd.read_csv('population.csv', encoding='sjis')
df_population = df_population[df_population['西暦（年）'] == 2015]
df_population = df_population[3:]
df_population = df_population[['都道府県コード','人口（総数）']]
df_population.columns = ['prefecture_code','population']
df_population = df_population.astype({'prefecture_code': int, 'population': int})
df_population.to_csv('population_done.csv',index = False)
# # vaccine
df_vaccine = pd.read_json('prefecture.ndjson',lines = True)
df_vaccine = df_vaccine[df_vaccine['status'] == 1]
df_vaccine = df_vaccine[['date','prefecture','count']]
df_vaccine.to_csv('vaccine.csv',index = False)





