from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


countries = pd.Series(['Colombia', 'Turkey', 'USA', 'Germany', 'Chile'], name='country')
print(countries)
print('\n', 'There are ', countries.shape[0], 'countries in this series.')

np.random.seed(123456)
data = pd.Series(np.random.normal(size=(countries.shape)), name='noise')
print(data)
print('\n', 'The average in this sample is ', data.mean())

df = pd.DataFrame([countries, data])
df = df.T
print('\n', df)

south_america = ['Colombia', 'Chile']
df.loc[df.country.apply(lambda x: x in south_america)]
df.country.apply(lambda x: x in south_america)
df['South America'] = df.country.apply(lambda x: x in south_america).astype(int)
df = df.set_index('country')
print(df)
df.plot()

pathout = './data/'

if not os.path.exists(pathout):
    os.mkdir(pathout)
    
pathgraphs = './graphs/'
if not os.path.exists(pathgraphs):
    os.mkdir(pathgraphs)

try:
    maddison_new = pd.read_stata(pathout + 'Maddison2018.dta')
    maddison_new_region = pd.read_stata(pathout + 'Maddison2018_region.dta')
    maddison_new_1990 = pd.read_stata(pathout + 'Maddison2018_1990.dta')
except:
    maddison_new = pd.read_stata('https://www.rug.nl/ggdc/historicaldevelopment/maddison/data/mpd2018.dta')
    maddison_new.to_stata(pathout + 'Maddison2018.dta', write_index=False, version=117)
    maddison_new_region = pd.read_stata('https://www.rug.nl/ggdc/historicaldevelopment/maddison/data/mpd2018_region_data.dta')
    maddison_new_region.to_stata(pathout + 'Maddison2018_region.dta', write_index=False, version=117)
    maddison_new_1990 = pd.read_stata('https://www.rug.nl/ggdc/historicaldevelopment/maddison/data/mpd2018_1990bm.dta')
    maddison_new_1990.to_stata(pathout + 'Maddison2018_1990.dta', write_index=False, version=117)

maddison_new['year'] = maddison_new.year.astype(int)

if not os.path.exists(pathout + 'Maddison_original.xls'):
    import urllib
    dataurl = "http://www.ggdc.net/maddison/Historical_Statistics/horizontal-file_02-2010.xls"
    urllib.request.urlretrieve(dataurl, pathout + 'Maddison_original.xls')

maddison_old_pop = pd.read_excel(pathout + 'Maddison_original.xls', sheet_name="Population", skiprows=2)
maddison_old_gdppc = pd.read_excel(pathout + 'Maddison_original.xls', sheet_name="PerCapita GDP", skiprows=2)
