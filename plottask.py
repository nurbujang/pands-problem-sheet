# plottask.py
# Author: Nur Bujang

# Week 8 task
# The task is to write a program that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range [0, 10], 
# on the one set of axes.
# add legends etc to the plot

# import modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

# this is so that the "random" numbers are the same each time
np.random.seed(1)
#create normal distribution curve
normData=np.random.normal(loc = 5, scale = 2, size = 1000)
plt.hist(normData, color='royalblue', edgecolor='#6495ED', linewidth=1)

# create data
x = np.array(range(1, 10))
# multiply each entry by itself twice to get y=x*x*x
y = x*x*x 

# customize plot, markertype, markersize, markercolor, linetype, linewidth, linecolor
plt.plot(x, y, marker = '*', ms = 10, mec = 'm', ls = '-.', linewidth = '2', color ='#B8860B', label = "$x^3$")
# declare font and font size
font1 = {'family':'fantasy', 'size':20}
font2 = {'family':'monospace', 'size':18}

# customize plot title and axis labels, x$^3$=$x^3$ for superscript
plt.title("Figure 1: h(x)=$x^3$ Plot", color ='#191970', fontdict = font1, fontweight='bold')
plt.xlabel("x", color ='#00008B', fontdict = font2, style='oblique', fontweight='bold')
# this code also rotates and creates a little space between y label and y-axis
plt.ylabel("y", color ='#00008B', fontdict = font2, style='oblique', fontweight='bold', rotation = 0, labelpad=12)

# customize legend using mpatches and mlines
royalblue_patch = mpatches.Patch(color='royalblue', edgecolor='#6495ED', linewidth=1, label='random values')
magenta_line = mlines.Line2D([], [], mec='magenta', marker='*', markersize=10, ls = '-.', linewidth = '2', color ='#B8860B')
plt.legend([royalblue_patch, magenta_line], ["random values", "$x^3$"], loc='upper left')

# add grid on y-axis
plt.grid(axis = 'y', color = '#8FBC8F', linestyle = '--', linewidth = 0.3)
# show plot
plt.show()
