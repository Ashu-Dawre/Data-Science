import matplotlib.pyplot as mpl

companies=['apple','microsoft','hp','dell','lenovo','acer','asus']
itemssold=[156,124,574,395,351,427,175]
clr=['red','green','blue','purple','magenta','cyan','teal']

mpl.bar(companies,itemssold,color=clr)
mpl.xlabel('Companies')
mpl.ylabel('Sold')
mpl.title('Sale in 2021')
mpl.show()