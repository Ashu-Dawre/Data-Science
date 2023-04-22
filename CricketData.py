import pandas
import matplotlib.pyplot as mpl

df=pandas.read_csv('england.csv')
mpl.plot(df['Overs'],df['Runrate'],color='blue')
mpl.scatter(df['Overs'],df['Runrate'],color='black')

df1=pandas.read_csv('india.csv')
mpl.plot(df1['Overs'],df1['Runrate'],color='red')
mpl.scatter(df1['Overs'],df1['Runrate'],color='green')

mpl.title('Runrate comparison after 10 overs')
mpl.show()
