"""
Created on Fri Feb  2 11:18:44 2018
@author: s1687599 (Python 3.6)
Description:
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.lines as lines

#%%=========================================================================%%#
fig=plt.figure(figsize=(5,4.5))
ax1=plt.subplot(111)

Data=[0.33,3.04,2.06,3.99,15.01,31.35,50.65,42.64,16.96,18.16,12.97,30.96,35.75,27.79,16.15,4.86,2.71,3.30,0,2.38,1.17,2.29,1.30,1.46,4.95,5.38,7.12,26.43,41.97,39.41,29.87,18.83,13.99,13.84,31.34,32.07,20.62,6.13,5.31,6.61,1.90]
MData=np.mean(Data)

n,bins,patches=plt.hist(Data,bins=10,normed=None,edgecolor='black',facecolor='steelblue',alpha=1,zorder=2)

L1 = ax1.add_artist(lines.Line2D((MData,MData),(0,20),linestyle='-',color='darkred',zorder=1))
#T1 = ax1.text(15.44+5,16.5,'Mean percentage intersection\nof linear line (15.44%)',ha='center',rotation=90,fontsize=10,color='darkred')
L2 = ax1.add_artist(lines.Line2D((31.71,31.71),(0,20),linestyle='-',color='darkgreen',zorder=1))
#T2 = ax1.text(31.71+5,17.5,'Percentage intersection of\nmodern drainage divide (31.71%)',ha='center',rotation=90,fontsize=10,color='darkgreen')
L3 = ax1.add_artist(lines.Line2D((50.75,50.75),(0,20),linestyle='-',color='darkgoldenrod',zorder=1))
#T3 = ax1.text(50.65+5,17.5,'Highest percentage intersection of\nlinear line (50.65%)',ha='center',rotation=90,fontsize=10,color='darkgoldenrod')

darkred_line=lines.Line2D([],[],color='darkred',markersize=15,label='Mean percentage\nintersection of\nlinear line (15.44%)')
darkgreen_line=lines.Line2D([],[],color='darkgreen',markersize=15, label='Percentage intersection\nof modern drainage\ndivide (31.71%)')
darkgoldenrod_line=lines.Line2D([],[],color='darkgoldenrod',markersize=15, label='Highest percentage\nintersection of\nlinear line (50.65%)')

leg1=plt.legend(handles=[darkred_line,darkgreen_line,darkgoldenrod_line],loc=1,bbox_to_anchor=(0.985,0.985),facecolor=(0.773,0.898,0.961),fancybox=True,edgecolor=(0,0,0,1),fontsize=8)

ax1.axis([0,100,0,16])
ax1.set_xlabel('Percentage intersection with massifs (%)')
ax1.set_ylabel('Frequency')

ax1.yaxis.grid(which='major',linestyle='--',color='k',alpha=0.5,zorder=0)
ax1.xaxis.grid(which='major',linestyle='--',color='k',alpha=0.5,zorder=0)