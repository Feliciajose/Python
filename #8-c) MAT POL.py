#8-c) MATPLOTLIB
frommatplotlib import pyplot as plt
# x axis values
x = [1,2,3,4,5,6]
# corresponding y axis values
y = [2, 4, 6, 8, 6, 4]
# plotting the points
plt.plot(x, y)
# naming the x axis
plt.xlabel('x-axis')
# naming the y axis
plt.ylabel('y-axis')
# Title to graph
plt.title('My First Graph')
# function to show the plot
plt.show()