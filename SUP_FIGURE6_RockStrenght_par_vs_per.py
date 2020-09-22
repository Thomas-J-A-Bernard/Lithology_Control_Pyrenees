"""
Created on Wed Jul 11 15:52:56 2018
@author: s1687599 (Python 3.6)
Description:
"""
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SCH_Pyr_MSed_Par = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_METASED_PARA.csv")
SCH_Pyr_MSed_Per = pd.read_csv("Z:\\Post-orogenic sediment flux to continental margins\\Schmidt_hammer_measurement\\SCH_PYRENEES_METASED_PER.csv")

Box_Data = [0]*2
Box_Data[0]=SCH_Pyr_MSed_Par.iloc[:,0]
Box_Data[1]=SCH_Pyr_MSed_Per.iloc[:,0]

fig1 = plt.figure(1,figsize=(4,4))
ax1 = fig1.add_subplot(111)

median_custom = dict(linestyle='-',linewidth=1.5,color='#FFB300')
mean_custom = dict(linestyle='-',linewidth=1.5,color='#A54747')
LIST = ['A','B']

bp1 = ax1.boxplot(Box_Data,showmeans=True,meanline=True,meanprops=mean_custom,medianprops=median_custom,labels=LIST,patch_artist=False,showfliers=False)

ax1.set_ylabel('Rock Strength (MPa)', fontsize=10)
ax1.set_xlabel('Lithology',fontsize=10) 