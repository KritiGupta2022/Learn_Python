# This program creates different types of graphs.

# x value : 5,7,8,7,2,17,2,9,4,11,12,9,6
#y value : 99,86,87,88,111,86,103,87,94,78,77,85,86

import matplotlib.pyplot as plt
import numpy as np



# line graph
def line():
    plt.plot(x,y)
    plt.show()


# Bar graph
def bar():
    plt.bar(x,y)
    plt.show()


# Histogram
def hist():
    a = np.random.normal(x)
    plt.hist(a)
    plt.show()


# Scatter graph
def scatter():
    plt.scatter(x, y)
    plt.show()

# Pie chart
def pie():
    plt.pie(y)
    plt.show() 
def choice():
    Choice= int(input("ENTER CHOICE BETWEEN 1 TO 5\n 1 FOR LINE GRAPH\n 2 FOR BAR GRAPH \n 3 FOR HISTOGRAM\n 4 FOR SCATTER GRAPH \n 5 FOR PIE CHART\n ENTER YOUR CHOICE :"))
    if Choice==1:
        line()
    elif Choice==2:
        bar()
    elif Choice==3:
        hist()
    elif Choice==4:
        scatter()
    elif Choice==5:
        pie()
    else:
        print("Enter valid choice !")
        choice()

x= list(map(int,input("Enter x values :").split(",")))
y= list(map(int,input("Enter y values :").split(",")))
n=str(input("Enter X label :"))
m=str(input("Enter Y label :"))
plt.xlabel(n)
plt.ylabel(m)
choice()
