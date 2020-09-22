"""
Created on Fri Jun 15 17:08:45 2018
@author: s1687599 (Python 3.6)
Description:
"""

#import matplotlib
#matplotlib.use("Agg")
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#%%=========================================================================%%#
#=========================== ROCK STRENGH DATA MANAGEMENT ====================#
SCH_Pyr_Gra = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_GRA_ALL.csv")
SCH_Pyr_Msed = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_METASED_ALL.csv")
SCH_Pyr_Sed = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_SED_ALL.csv")
SCH_Pyr_UncSed = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_UNCSED_ALL.csv")
SCH_Pyr_SilSed = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_SILSED_ALL.csv")
SCH_Pyr_CalSed = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_CalSED_ALL.csv")

Box_Data = [0]*6
Box_Data[5]=SCH_Pyr_Gra.iloc[:,0]
Box_Data[4]=SCH_Pyr_Msed.iloc[:,0]
Box_Data[3]=SCH_Pyr_Sed.iloc[:,0]
Box_Data[2]=SCH_Pyr_CalSed.iloc[:,0]
Box_Data[1]=SCH_Pyr_SilSed.iloc[:,0]
Box_Data[0]=SCH_Pyr_UncSed.iloc[:,0]

#%%=========================================================================%%#
#=========================== MCHI DATASET MANAGEMENT =========================#
Path = "Z:\LSDTopoTools\Topographic_projects\LSDTT_Pyrenees_data\Geology_data_workflow_Corrected/"
File = "Extract_Mountain_Pyrenees_Geology.csv"

DataFrame = pd.read_csv(Path+File)
print(DataFrame.columns.values)
m = 8

df_1 = DataFrame[DataFrame["geology"]==1]; df_1.columns = ['Unconsolidated Sediments' if x=='m_chi' else x for x in df_1.columns]
df_2 = DataFrame[DataFrame["geology"]==2]; df_2.columns = ['Mixed Sedimentary Rocks' if x=='m_chi' else x for x in df_2.columns]
#df_3_6 = DataFrame[DataFrame["geology"].isin([3,6])]; df_3_6.columns = ['Volcanic Rocks' if x=='m_chi' else x for x in df_3_6.columns]
df_4_7_9 = DataFrame[DataFrame["geology"].isin([4,7,9])]; df_4_7_9.columns = ['Plutonic Rocks' if x=='m_chi' else x for x in df_4_7_9.columns]
df_5 = DataFrame[DataFrame["geology"]==5]; df_5.columns = ['Metamorphic Rocks' if x=='m_chi' else x for x in df_5.columns]
df_8 = DataFrame[DataFrame["geology"]==8]; df_8.columns = ['Siliciclastic Sedimentary Rocks' if x=='m_chi' else x for x in df_8.columns]
df_10 = DataFrame[DataFrame["geology"]==10]; df_10.columns = ['Carbonate Sedimentary Rocks' if x=='m_chi' else x for x in df_10.columns]
#df_11 = DataFrame[DataFrame["geology"]==11]; df_11.columns = ['Water Body' if x=='m_chi' else x for x in df_11.columns]

data_to_plot = [df_1["Unconsolidated Sediments"],df_2["Mixed Sedimentary Rocks"],df_4_7_9["Plutonic Rocks"],df_5["Metamorphic Rocks"],df_8["Siliciclastic Sedimentary Rocks"],df_10["Carbonate Sedimentary Rocks"]]
litho = [df_1.columns.values[m],df_2.columns.values[m],df_4_7_9.columns.values[m],df_5.columns.values[m],df_8.columns.values[m],df_10.columns.values[m]]
LIST = ['A','B','C','D','E','F']
BoxColor=['#C8C864','#9D78C1','#AF5A5A','#A6835F','#F3C793','#6E899B']

should_restart = True
while should_restart:
  should_restart = False  
  for i in range (0,np.size(data_to_plot)):
    if np.size(data_to_plot[i]) == 0:
      del data_to_plot[i];del litho[i];del LIST[i];del BoxColor[i]
      should_restart = True
      break

med = [np.nan]*np.size(data_to_plot)
for i in range (0,np.size(data_to_plot)):
  med[i]=np.mean(data_to_plot[i])

data_to_plot2 = [np.nan]*np.size(data_to_plot)
litho2 = [np.nan]*np.size(data_to_plot)
LIST2 = [np.nan]*np.size(data_to_plot)
BoxColor2 = [np.nan]*np.size(data_to_plot)

tsup=10000
tinf=0
for i in range (0,np.size(data_to_plot)):
  for j in range (0,np.size(data_to_plot)):
    if med[j] < tsup and med[j] > tinf:
      tsup=med[j]
      compt1=j
      data_to_plot2[i] = data_to_plot[compt1]
      litho2[i] = litho[compt1]
      LIST2[i] = LIST[compt1]
      BoxColor2[i] = BoxColor[compt1]
  tsup=10000
  tinf=med[compt1]
  
#%%=========================================================================%%#
#==========================ELEVATION DATA MANAGEMENT==========================#
df_1_E = DataFrame[DataFrame["geology"]==1]; df_1_E.columns = ['Unconsolidated Sediments' if x=='elevation' else x for x in df_1_E.columns]
df_2_E = DataFrame[DataFrame["geology"]==2]; df_2_E.columns = ['Mixed Sedimentary Rocks' if x=='elevation' else x for x in df_2_E.columns]
#df_3_6_E = DataFrame[DataFrame["geology"].isin([3,6])]; df_3_6_E.columns = ['Volcanic Rocks' if x=='elevation' else x for x in df_3_6_E.columns]
df_4_7_9_E = DataFrame[DataFrame["geology"].isin([4,7,9])]; df_4_7_9_E.columns = ['Plutonic Rocks' if x=='elevation' else x for x in df_4_7_9_E.columns]
df_5_E = DataFrame[DataFrame["geology"]==5]; df_5_E.columns = ['Metamorphic Rocks' if x=='elevation' else x for x in df_5_E.columns]
df_8_E = DataFrame[DataFrame["geology"]==8]; df_8_E.columns = ['Siliciclastic Sedimentary Rocks' if x=='elevation' else x for x in df_8_E.columns]
df_10_E = DataFrame[DataFrame["geology"]==10]; df_10_E.columns = ['Carbonate Sedimentary Rocks' if x=='elevation' else x for x in df_10_E.columns]
#df_11_E = DataFrame[DataFrame["geology"]==11]; df_11_E.columns = ['Water Body' if x=='elevation' else x for x in df_11_E.columns]

data_to_plot_E = [df_1_E["Unconsolidated Sediments"],df_2_E["Mixed Sedimentary Rocks"],df_4_7_9_E["Plutonic Rocks"],df_5_E["Metamorphic Rocks"],df_8_E["Siliciclastic Sedimentary Rocks"],df_10_E["Carbonate Sedimentary Rocks"]]
litho_E = [df_1_E.columns.values[m],df_2_E.columns.values[m],df_4_7_9_E.columns.values[m],df_5_E.columns.values[m],df_8_E.columns.values[m],df_10_E.columns.values[m]]
LIST_E = ['A','B','C','D','E','F']
BoxColor_E=['#C8C864','#9D78C1','#AF5A5A','#A6835F','#F3C793','#6E899B']

should_restart = True
while should_restart:
  should_restart = False  
  for i in range (0,np.size(data_to_plot_E)):
    if np.size(data_to_plot_E[i]) == 0:
      del data_to_plot_E[i];del litho_E[i];del LIST_E[i];del BoxColor_E[i]
      should_restart = True
      break

med = [np.nan]*np.size(data_to_plot_E)
for i in range (0,np.size(data_to_plot_E)):
  med[i]=np.mean(data_to_plot_E[i])

data_to_plot2_E = [np.nan]*np.size(data_to_plot_E)
litho2_E = [np.nan]*np.size(data_to_plot_E)
LIST2_E = [np.nan]*np.size(data_to_plot_E)
BoxColor2_E = [np.nan]*np.size(data_to_plot_E)

tsup=10000
tinf=0
for i in range (0,np.size(data_to_plot_E)):
  for j in range (0,np.size(data_to_plot_E)):
    if med[j] < tsup and med[j] > tinf:
      tsup=med[j]
      compt1=j
      data_to_plot2_E[i] = data_to_plot_E[compt1]
      litho2_E[i] = litho_E[compt1]
      LIST2_E[i] = LIST_E[compt1]
      BoxColor2_E[i] = BoxColor_E[compt1]
  tsup=10000
  tinf=med[compt1]


#%%=========================================================================##%
fig1 = plt.figure(1,figsize=(10,4))

ax3 = fig1.add_subplot(131)
ax2 = fig1.add_subplot(132)
ax1 = fig1.add_subplot(133)

median_custom = dict(linestyle='-',linewidth=1.5,color='#FFB300')
mean_custom = dict(linestyle='-',linewidth=1.5,color='#A54747')

bp1 = ax1.boxplot(Box_Data,showmeans=True,meanline=True,meanprops=mean_custom,medianprops=median_custom,labels=LIST2,patch_artist=True,showfliers=False)
for patch, color in zip(bp1['boxes'],BoxColor2):
  patch.set_facecolor(color)

bp2 = ax2.boxplot(data_to_plot2_E,showmeans=True,meanline=True,meanprops=mean_custom,medianprops=median_custom,labels=LIST2,patch_artist=True,showfliers=False)
for patch, color in zip(bp2['boxes'],BoxColor2):
  patch.set_facecolor(color)

bp3 = ax3.boxplot(data_to_plot2,showmeans=True,meanline=True,meanprops=mean_custom,medianprops=median_custom,labels=LIST2_E,patch_artist=True,showfliers=False)
for patch, color in zip(bp3['boxes'],BoxColor2_E):
  patch.set_facecolor(color)

ax1.set_ylabel('Rebound value (R)', fontsize=11)
ax1.set_xlabel('Lithology',fontsize=10) 
ax2.set_ylabel('Elevation (m)', fontsize=11)
ax2.set_xlabel('Lithology',fontsize=11)
ax3.set_ylabel('k$_{sn}$', fontsize=11)
ax3.set_xlabel('Lithology',fontsize=11)

ax3.text(0.125, 0.90, 'A', verticalalignment='bottom', horizontalalignment='right', transform=ax3.transAxes, fontsize=12, fontweight='bold')
ax2.text(0.125, 0.90, 'B', verticalalignment='bottom', horizontalalignment='right', transform=ax2.transAxes, fontsize=12, fontweight='bold')
ax1.text(0.125, 0.90, 'C', verticalalignment='bottom', horizontalalignment='right', transform=ax1.transAxes, fontsize=12, fontweight='bold')

ax1.text(0.875, 24.5, 'n = 30', fontsize=10, rotation=90, color='darkred')
ax1.text(1.875, 60.5, 'n = 150', fontsize=10, rotation=90, color='darkred')
ax1.text(2.875, 62, 'n = 90', fontsize=10, rotation=90, color='darkred')
ax1.text(3.625, 28, 'n = 120', fontsize=10, rotation=90, color='darkred')
ax1.text(4.875, 21, 'n = 90', fontsize=10, rotation=90, color='darkred')
ax1.text(5.875, 26, 'n = 106', fontsize=10, rotation=90, color='darkred')

ax3.text(0.875, 169, 'n = 48595', fontsize=10, rotation=90, color='darkred')
ax3.text(1.875, 272, 'n = 125368', fontsize=10, rotation=90, color='darkred')
ax3.text(2.875, 288, 'n = 235103', fontsize=10, rotation=90, color='darkred')
ax3.text(3.625, 246, 'n = 96026', fontsize=10, rotation=90, color='darkred')
ax3.text(4.625, 253, 'n = 96353', fontsize=10, rotation=90, color='darkred')
ax3.text(5.625, 258, 'n = 41536', fontsize=10, rotation=90, color='darkred')
   
plt.subplots_adjust(left=0.075, bottom=0.135, right=0.975, top=0.95, wspace=0.4, hspace=None)

#fig1.savefig("Z:\Post-orogenic sediment flux to continental margins\Publication_Report\Paper_Control_of_lithology_on_landscape_of_the post-orogenesis_of_Pyrenees_TB-HS\FIGURE_V4.0\FIGURE4_3Plot_RockStrenght+mChi+Elevation_vs_Lithology_v4.0.jpg",dpi=1000)
#fig1.savefig("Z:\Post-orogenic sediment flux to continental margins\Publication_Report\Paper_Control_of_lithology_on_landscape_of_the post-orogenesis_of_Pyrenees_TB-HS\FIGURE_V4.0\FIGURE4_3Plot_RockStrenght+mChi+Elevation_vs_Lithology_v4.0.pdf",dpi=1000)