import matplotlib.pyplot as plt

categories = ['Category A','Category B','Category C','Category D']
values = [15,30,22,40]
plt.bar(categories,values,color="pink")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar graph")
plt.show()
