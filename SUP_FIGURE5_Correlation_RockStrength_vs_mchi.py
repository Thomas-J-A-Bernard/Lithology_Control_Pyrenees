"""
Created on Tue Dec  4 10:11:11 2018
@author: s1687599 (Python 3.6)
Description:
"""

#import matplotlib
#matplotlib.use("Agg")
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

#%%=========================================================================%%#
#=========================== ROCK STRENGH DATA MANAGEMENT ====================#
SCH_Pyr_Gra = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_GRA_ALL.csv")
SCH_Pyr_Msed = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_METASED_ALL.csv")
SCH_Pyr_Sed = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_SED_ALL.csv")
SCH_Pyr_UncSed = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_UNCSED_ALL.csv")
SCH_Pyr_SilSed = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_SILSED_ALL.csv")
SCH_Pyr_CarSed = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_CalSED_ALL.csv")

Box_Data = [0]*6
Box_Data[5]=SCH_Pyr_Gra.iloc[:,0]
Box_Data[4]=SCH_Pyr_Msed.iloc[:,0]
Box_Data[3]=SCH_Pyr_Sed.iloc[:,0]
Box_Data[2]=SCH_Pyr_CarSed.iloc[:,0]
Box_Data[1]=SCH_Pyr_SilSed.iloc[:,0]
Box_Data[0]=SCH_Pyr_UncSed.iloc[:,0]

Rock_Strength_Mean = [np.nan]*np.size(Box_Data)
Rock_Strength_Median = [np.nan]*np.size(Box_Data)
for i in range(0,np.size(Box_Data)):
  Rock_Strength_Mean[i] = np.mean(Box_Data[i])
  Rock_Strength_Median[i] = np.median(Box_Data[i])

#%%=========================================================================%%#
#=========================== MCHI DATASET MANAGEMENT =========================#
Path = "Z:\LSDTopoTools\Topographic_projects\LSDTT_Pyrenees_data\Geology_data_workflow_Corrected/"
File = "Extract_Mountain_Pyrenees_Geology.csv"

DataFrame = pd.read_csv(Path+File)
print(DataFrame.columns.values)
m = 8

df_1 = DataFrame[DataFrame["geology"]==1]; df_1.columns = ['Unconsolidated Sediments' if x=='m_chi' else x for x in df_1.columns]
df_2 = DataFrame[DataFrame["geology"]==2]; df_2.columns = ['Mixed Sedimentary Rocks' if x=='m_chi' else x for x in df_2.columns]
df_4_7_9 = DataFrame[DataFrame["geology"].isin([4,7,9])]; df_4_7_9.columns = ['Plutonic Rocks' if x=='m_chi' else x for x in df_4_7_9.columns]
df_5 = DataFrame[DataFrame["geology"]==5]; df_5.columns = ['Metamorphic Rocks' if x=='m_chi' else x for x in df_5.columns]
df_8 = DataFrame[DataFrame["geology"]==8]; df_8.columns = ['Siliciclastic Sedimentary Rocks' if x=='m_chi' else x for x in df_8.columns]
df_10 = DataFrame[DataFrame["geology"]==10]; df_10.columns = ['Carbonate Sedimentary Rocks' if x=='m_chi' else x for x in df_10.columns]

data_to_plot = [df_1["Unconsolidated Sediments"],df_8["Siliciclastic Sedimentary Rocks"],df_10["Carbonate Sedimentary Rocks"],df_2["Mixed Sedimentary Rocks"],df_5["Metamorphic Rocks"],df_4_7_9["Plutonic Rocks"]]

Mchi_Mean = [np.nan]*np.size(data_to_plot)
Mchi_Median = [np.nan]*np.size(data_to_plot)
for i in range(0,np.size(data_to_plot)):
  Mchi_Mean[i] = np.mean(data_to_plot[i])
  Mchi_Median[i] = np.median(data_to_plot[i])
  
#%%=========================================================================%%#

Correlation_Mean = np.zeros((6,2))
Correlation_Median = np.zeros((6,2))
for i in range(0,6):
  Correlation_Mean[i,1] = Mchi_Mean[i]; Correlation_Mean[i,0] = Rock_Strength_Mean[i]
  Correlation_Median[i,1] = Mchi_Median[i]; Correlation_Median[i,0] = Rock_Strength_Median[i]
  
x1, y1 = Correlation_Mean.T
x2, y2 = Correlation_Median.T
  
#%%=========================================================================%%#
#=========================== CORRELATION FIGURE ==============================#
  
fig1 = plt.figure(1, figsize = (5,4))
ax1 = fig1.add_subplot(111)

slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(x1,y1)
Line_Mean = slope1*x1+intercept1
L1 = ax1.plot(x1, Line_Mean, linestyle='--', color='k',zorder=1)

slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(x2,y2)
Line_Median = slope2*x2+intercept2
L1 = ax1.plot(x2, Line_Median, linestyle='-.', color='k',zorder=1)

MN0 = ax1.scatter(Correlation_Mean[0,0], Correlation_Mean[0,1], s=60, c='#C8C864', marker='D', edgecolors='k',zorder=2)
MN1 = ax1.scatter(Correlation_Mean[1,0], Correlation_Mean[1,1], s=60, c='#F3C793', marker='D', edgecolors='k',zorder=2)
MN2 = ax1.scatter(Correlation_Mean[2,0], Correlation_Mean[2,1], s=60, c='#6E899B', marker='D', edgecolors='k',zorder=2)
MN3 = ax1.scatter(Correlation_Mean[3,0], Correlation_Mean[3,1], s=60, c='#9D78C1', marker='D', edgecolors='k',zorder=2)
MN4 = ax1.scatter(Correlation_Mean[4,0], Correlation_Mean[4,1], s=60, c='#A6835F', marker='D', edgecolors='k',zorder=2)                 
MN5 = ax1.scatter(Correlation_Mean[5,0], Correlation_Mean[5,1], s=60, c='#AF5A5A', marker='D', edgecolors='k',zorder=2)

MD0 = ax1.scatter(Correlation_Median[0,0], Correlation_Median[0,1], s=70, c='#C8C864', marker='o', edgecolors='k',zorder=2)
MD1 = ax1.scatter(Correlation_Median[1,0], Correlation_Median[1,1], s=70, c='#F3C793', marker='o', edgecolors='k',zorder=2)
MD2 = ax1.scatter(Correlation_Median[2,0], Correlation_Median[2,1], s=70, c='#6E899B', marker='o', edgecolors='k',zorder=2)
MD3 = ax1.scatter(Correlation_Median[3,0], Correlation_Median[3,1], s=70, c='#9D78C1', marker='o', edgecolors='k',zorder=2)
MD4 = ax1.scatter(Correlation_Median[4,0], Correlation_Median[4,1], s=70, c='#A6835F', marker='o', edgecolors='k',zorder=2)                 
MD5 = ax1.scatter(Correlation_Median[5,0], Correlation_Median[5,1], s=70, c='#AF5A5A', marker='o', edgecolors='k',zorder=2)

ax1.set_xlabel('Rebound value (R)', fontsize=11)
ax1.set_ylabel('k$_{sn}$',fontsize=12)              
ax1.yaxis.grid(which='major',linestyle='--',color='k',alpha=0.5,zorder=0); ax1.xaxis.grid(which='major',linestyle='--',color='k',alpha=0.5,zorder=0)
ax1.axis([8,55,10,135])
plt.subplots_adjust(left=0.14, bottom=0.135, right=0.975, top=0.96, wspace=0.4, hspace=None)



