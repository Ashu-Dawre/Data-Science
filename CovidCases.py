import matplotlib.pyplot as mpl

month=['Jan','Feb','Mar','Apr','May','Jun']
cases=[39000,28000,67000,85000,72000,41000]
deaths=[4700,3800,7900,12700,6200,3100]

mpl.plot(month,cases,color='blue')
mpl.scatter(month,cases,color='black')

mpl.plot(month,deaths,color='red')
mpl.scatter(month,deaths,color='green')
mpl.show()