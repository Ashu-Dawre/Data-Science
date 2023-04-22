import matplotlib.pyplot as mpl

companies=['apple','microsoft','hp','dell','lenovo','acer','asus']
itemssold=[156,124,574,395,351,427,175]

mpl.scatter(companies,itemssold,color='green')
mpl.xlabel('Companies')
mpl.ylabel('Sold')
mpl.title('Laptop sale in 2021')
mpl.grid(True)
mpl.legend('Sales')
mpl.show()