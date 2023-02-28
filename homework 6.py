# PPHA 30535
# Spring 2022
# Homework 6

# Buwen Zhang

# Buwen Zhang
# buwenz

# Due date: Sunday May 15th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_plot.png", "q2_plot.png", etc. If a question calls
# for more than one plot, name them "q1a_plot", "q1b_plot", etc.

#NOTE: If no specific library is called for by the question, then you may freely
# use Matplotlib, Pandas, Seaborn, or a combination to answer the question.

# Question 1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis labels are legible.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]

fig, ax = plt.subplots()
ax.scatter(x, y1, color='blue', linestyle='dotted', label='y1')
ax.plot(x, y2, color='green', linestyle='solid', label='y2')
plt.legend(loc='upper right')
plt.savefig('q1_plot.png', dpi=300)


# Question 2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.

fig, ax = plt.subplots()
x = np.linspace(0, 9, 100)
y1 = x
y2 = -x + 9
ax.plot(x, y1, 'b-', lw=3, label='Blue')
ax.plot(x, y2, 'r-', lw=3, label='Red')
ax.legend(loc='center left')
ax.set_title('X marks the spot')
fig.show()
plt.savefig('q2_plot.png', dpi=300)

# Question 3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.

data = pd.read_csv('mpg.csv')
x = data['displacement']
y = data['mpg']
fig, ax = plt.subplots()
ax.scatter(x, y, color='blue', s=5, label='mpg')
ax.set_title('displacement vs mpg')
ax.set_xlabel('displacement')
ax.set_ylabel('MPG')
plt.legend(loc='best')
plt.savefig('q3a_plot.png', dpi=300) 
# from the plot we can clearly observe that a car with an engine 
# that has a higher displacement will get worse gas 
# mileage than one that has a smaller displacement (the hypothesis is true).

# for mpg against horsepower and weight
x = data['horsepower']
y = data['mpg']
fig, ax = plt.subplots()
ax.scatter(x, y, color='blue', s=5, label='mpg')
ax.set_title('horsepower vs mpg')
ax.set_xlabel('horsepower')
ax.set_ylabel('MPG')
plt.legend(loc='best')
plt.savefig('q3b_plot.png', dpi=300) 

x = data['weight']
y = data['mpg']
fig, ax = plt.subplots()
ax.scatter(x, y, color='blue', s=5, label='mpg')
ax.set_title('weight vs mpg')
ax.set_xlabel('weight')
ax.set_ylabel('MPG')
plt.legend(loc='best')
plt.savefig('q3c_plot.png', dpi=300) 

# Question 4: Continuing from question 3, create a scatter plot with mpg
# on the y-axis and cylinders on the x-axis.  Explain what is wrong with this
# plot with a one-line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.

x = data['cylinders']
y = data['mpg']
fig, ax = plt.subplots()
ax.scatter(x, y, color='green', s=5, label='mpg')
ax.set_xlabel('cylinders')
ax.set_ylabel('MPG')
plt.legend(loc='best')
plt.savefig('q4a_plot.png', dpi=300)

#  As the values of cylinders are discrete, the scatter points always fall on some vertical lines

import seaborn as sns


ax = sns.boxplot(x='cylinders', y='mpg', data=data)
plt.savefig('q4b_plot.png', dpi=300)

# Question 5: Continuing from question 3, create a two-by-two grid of
# subplots, where each one has mpg on the y-axis and one of displacement,
# horsepower, weight, and acceleration on the x-axis.  To clean up this 
# plot, remove the y-axis labels on the right two plots - the scale will 
# already be aligned because the mpg values are the same.

fig, axes = plt.subplots(2, 2)
axes[0][0].scatter(data['displacement'], data['mpg'], color='blue', s=3, label='mpg')
axes[0][0].set_xlabel('displacement')
axes[0][0].set_ylabel('MPG')

axes[0][1].scatter(data['horsepower'], data['mpg'], color='red', s=3, label='mpg')
axes[0][1].set_xlabel('horsepower')
axes[0][1].get_yaxis().set_visible(False)

axes[1][0].scatter(data['weight'], data['mpg'], color='green', s=3, label='mpg')
axes[1][0].set_xlabel('weight')
axes[1][0].set_ylabel('MPG')

axes[1][1].scatter(data['acceleration'], data['mpg'], color='purple', s=3, label='mpg')
axes[1][1].set_xlabel('acceleration')
axes[1][1].get_yaxis().set_visible(False)

plt.subplots_adjust(wspace=0, hspace=0.3)
plt.savefig('q5_plot.png', dpi=300)

# Question 6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot.

grouped = data.groupby(['origin'])
ax = grouped.mean()['mpg'].plot.bar(rot=0)
ax.set_ylabel('MPG')
fig = ax.get_figure()
plt.savefig('q6_plot.png', dpi=300)

# Question 7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.

ax = sns.stripplot(x='displacement', y='mpg', hue='origin', data=data, jitter=0.1, size=4)
plt.savefig('q7_plot.png', dpi=300)


