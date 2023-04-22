import matplotlib.pyplot as mpl
import pandas

df=pandas.read_csv('covid-usa.csv')
df1=df[['month','cases']]
#print(df1)

mpl.plot(df1['month'],df1['cases'],color='blue')
mpl.scatter(df1['month'],df1['cases'],color='black')

df=pandas.read_csv('covid-usa.csv')
df2=df[['month','deaths']]
#print(df2)

mpl.plot(df2['month'],df2['deaths'],color='red')
mpl.scatter(df2['month'],df2['deaths'],color='green')

mpl.show()

