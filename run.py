#!/usr/bin/env python

import os
import os.path as op
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import plotly.graph_objs as go
import seaborn as sns

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("my_file",
                    type=str,
                    help="Path to the input csv file.")

args = parser.parse_args()

my_file = args.my_file

#data = pd.read_csv(my_csv_file, sep='\s+|,', header=None)
#print(data.head())

#print(data.shape)


# Add headers to the table
header_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
'MEDV']
data = pd.read_csv(my_file, sep='\s+|,', header=None, names=header_names)

print(data.head())

sns.set(style='darkgrid', context='notebook')
cols = ["CRIM", "AGE", "TAX", "PTRATIO", "LSTAT", "MEDV"]

plt.figure(figsize=(18,12))
plt.scatter(data.CRIM, data.MEDV, color='blue', marker="v", label = 'CRIM')
plt.scatter(data.AGE, data.MEDV, color='green', marker="s", label = 'AGE')
plt.scatter(data.TAX, data.MEDV, color='red', marker="p", label = 'TAX')
plt.scatter(data.PTRATIO, data.MEDV, color='orange', marker="h", label = 'PTRATIO')
plt.scatter(data.LSTAT, data.MEDV, color='Yellow', marker="D", label = 'LSTAT')

plt.title('Few Factors that affect housing price')
plt.xlabel("Factors affect housing price")
plt.ylabel("MEDV")
plt.legend()
plt.savefig("Few_Factors.png")
plt.show()

plt.figure(figsize=(10,10))
cm = np.corrcoef(data[cols].values.T)
sns.set(font_scale=1.5)
hm = sns.heatmap(cm,cbar=True,annot=True,square=True,fmt='.2f',annot_kws={'size':15},yticklabels=cols,xticklabels=cols)
plt.savefig("heatmap.png")
plt.show()


#VISUALIZE DATA:

# Visulaize Histogram of each feature
# - histogram AGE colum

#plt.figure(figsize=(10, 10))
#plt.hist(data.iloc[:, 6], bins=10, rwidth=0.9)
#plt.savefig("histo_age.png", dpi=100)
#plt.show()

# - Scatter Age&MEDV
#plt.scatter(data.iloc[:, 6], data.iloc[:, -1])
#plt.savefig("scatter_age_medv", dpi=100)
#plt.show()


#from plotly.offline import iplot, init_notebook_mode
#init_notebook_mode()
#ply.offline.init_notebook_mode(connected=True)
#cols = ["CRIM", "AGE", "TAX", "PTRATIO", "LSTAT"
#trace = go.Scatter(
#    x = )
#ply.plot({"data": [go.Scatter(x=[1,2,3,4], y=[4,3,2,1])], "layout": go.Layout(title="Housing data")}, auto_open=True)
