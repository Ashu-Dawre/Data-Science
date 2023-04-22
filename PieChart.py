import matplotlib.pyplot as mpl

companies=['apple','microsoft','hp','dell','lenovo','acer','asus']
itemssold=[156,124,574,395,351,427,175]

mpl.pie(itemssold,labels=companies)
mpl.title('Sale in 2021')
mpl.show()