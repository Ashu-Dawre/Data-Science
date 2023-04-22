import matplotlib.pyplot as mpl

companies=['apple','microsoft','hp','dell','lenovo','acer','asus']
itemssold=[156,124,574,395,351,427,175]
print(type(companies))
print(type(itemssold))
mpl.plot(companies,itemssold,color='red',linestyle='dashdot')
mpl.xlabel('Companies')
mpl.ylabel('Sold')
mpl.title('Laptop Sale in 2021')
mpl.grid(True)
mpl.show()