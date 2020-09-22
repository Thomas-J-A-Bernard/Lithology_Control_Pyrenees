"""
Script to test the effect of different concavity indexes to compare k_sn.

Modified by T.B. after B.G. 04/02/2018

"""

# This first step is a debugging step, the school server does not support default matplotlib configuration so we have to manually define the graphic backend
#import matplotlib
#matplotlib.use("Agg")
# you can ignore it

# Matplotlib for plotting
from matplotlib import pyplot as plt
# Pandas to manage the data
import pandas as pd
# os deals with system operations such as creating folder or checking if a files exists
import os
# scipy
from scipy import stats as st
# Numpy
import numpy as np

def load_the_dataframe(path = "/home/s1687599/Datastore/LSDTopoTools/Topographic_projects/LSDTT_Pyrenees_data/m_over_n_analyses/PYRENEES/sensitivity_test_movern/",common_name_of_csv_with_geology = "Extract_Basin_PYRENEES_Geology.csv", conc =[0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70]):
    """
        this function read the entire dataset and concatenate all the m/n dataframes in a single one to make the plotting easy. 
    """

    # Iterate through all the concavity indexes
    for concavity in conc:
        #load the current file
        print("dealing with theta = " + str(concavity))
        tdf = pd.read_csv(path+"movern_%s/%s" %(concavity, common_name_of_csv_with_geology))
        tdf["concavity_index"] = pd.Series(data = concavity, index = tdf.index)
        tdf = add_stats(tdf)

        # creating the final dataframe if this is the first iteration, otherwise concatenating
        if(concavity == conc[0]):
            df = tdf.copy()
        else:
            df = pd.concat([df,tdf],ignore_index = True)

    return df

def group_geologies(df, dictionnary_of_litho = {"Plutonic R.": [4,7,9], "Metamorphic r.":[5], "Volcanic r.": [3,6], "Mixed s.r.": [2], "Carbonate s.r.": [10], "Siliciclastic s.r.": [8], "Unconsolidated s.r.": [1], "Water Body": [11]}):

    """
        This function group the requested geology by creating a new column with the geological information
    """

    # First I define the new group names and the associated OLD lithokeyS
    geocode = dictionnary_of_litho
    # Creating the new column
    df["Classification"] = pd.Series(data = "none", index = df.index)

    # assigning the groupping values
    for key in geocode:

        val = geocode[key]
        df["Classification"][df["geology"].isin(val)] = key


    # cleaning the df
    if(df[df["Classification"] == "none"].shape[0]>0):
        print("I am removing %s no data"% df[df["Classification"] == "none"].shape[0])
        df = df[df["Classification"] != "none"]


    return df

def add_stats(df):
    """
        THis function adds stat columns to deal with data spreadings and so on
    """

    df["z_score_glob"] = pd.Series( data = st.mstats.zscore(df["m_chi"].values), index = df.index)
    df["percentile"] = pd.Series( data = 0, index = df.index)

    this_percentile = 0
    last_percentile = df["m_chi"].min()
    for perc in range(1,101):
        this_percentile = (np.percentile(df["m_chi"].values,perc))
        df["percentile"][(df["m_chi"]<this_percentile) & (df["m_chi"]>=last_percentile)] = perc
        last_percentile = this_percentile




    return df





###### Plotting functions ######

def BandW_litho(df):
    """
        Print a box and whisker figure with ksn in function of lithologies for each concavity indexes
        
    """
    # check if a directory exists for the chi plots. If not then make it.
    out_directory = './sensitivity_concav/'

    if not os.path.isdir(out_directory):
        print("I am creating the river_plot/ directory to save your figures")
        os.makedirs(out_directory)

    for theta in df["concavity_index"].unique(): 

        tdf = df[df["concavity_index"] == theta]
        fig = plt.figure(1, facecolor = "white", figsize=(9,7))

        gs = plt.GridSpec(100,100,bottom=0.15,left=0.10,right=0.95,top=0.95)
        ax1 = fig.add_subplot(gs[0:100,0:100], facecolor = "None")

        data_to_plot = []
        names = []

        for geol in tdf["Classification"].unique():
            tdf2 = tdf["m_chi"][tdf["Classification"] == geol]
            data_to_plot.append(tdf2)
            names.append(geol+"\nn = " + str(tdf2.shape[0]))


        
        bp = ax1.boxplot(data_to_plot, labels = names, patch_artist = True)

        ## change outline color, fill color and linewidth of the boxes
        for box in bp['boxes']:
            # change outline color
            box.set( color='k', linewidth=1.5)
            # change fill color
            box.set( facecolor = '#848484' )

        ## change color and linewidth of the whiskers
        for whisker in bp['whiskers']:
            whisker.set(color='k', linewidth=1)

        ## change color and linewidth of the caps
        for cap in bp['caps']:
            cap.set(color='#2C2C2C', linewidth=1)

        ## change color and linewidth of the medians
        for median in bp['medians']:
            median.set(color='#E0E0E0', linewidth=1)

        ## change the style of fliers and their fill
        for flier in bp['fliers']:
            flier.set(marker='+', color='#A0A0A0', alpha=0.5)

        ax1.set_ylabel(r"$k_{sn}$")
        ax1.tick_params(labelsize = 6)

        plt.title(r"$k_{sn}$ distribution for $\theta =$ %s"%(theta) )

        plt.savefig(out_directory + "ksn_litho_%s.png" %(theta), dpi = 500)
        plt.clf()

def BandW_litho_z_score(df):
    """
        Print a box and whisker figure with ksn in function of lithologies for each concavity indexes
        
    """
    # check if a directory exists for the chi plots. If not then make it.
    out_directory = './sensitivity_concav/'

    if not os.path.isdir(out_directory):
        print("I am creating the river_plot/ directory to save your figures")
        os.makedirs(out_directory)

    for theta in df["concavity_index"].unique(): 

        tdf = df[df["concavity_index"] == theta]
        fig = plt.figure(1, facecolor = "white", figsize=(9,7))

        gs = plt.GridSpec(100,100,bottom=0.15,left=0.10,right=0.95,top=0.95)
        ax1 = fig.add_subplot(gs[0:100,0:100], facecolor = "None")

        data_to_plot = []
        names = []

        for geol in tdf["Classification"].unique():
            tdf2 = tdf["z_score_glob"][tdf["Classification"] == geol]
            data_to_plot.append(tdf2)
            names.append(geol+"\nn = " + str(tdf2.shape[0]))


        
        bp = ax1.boxplot(data_to_plot, labels = names, patch_artist = True)

        ## change outline color, fill color and linewidth of the boxes
        for box in bp['boxes']:
            # change outline color
            box.set( color='k', linewidth=1.5)
            # change fill color
            box.set( facecolor = '#848484' )

        ## change color and linewidth of the whiskers
        for whisker in bp['whiskers']:
            whisker.set(color='k', linewidth=1)

        ## change color and linewidth of the caps
        for cap in bp['caps']:
            cap.set(color='#2C2C2C', linewidth=1)

        ## change color and linewidth of the medians
        for median in bp['medians']:
            median.set(color='#E0E0E0', linewidth=1)

        ## change the style of fliers and their fill
        for flier in bp['fliers']:
            flier.set(marker='+', color='#A0A0A0', alpha=0.5)

        ax1.set_ylabel("z-score")
        ax1.tick_params(labelsize = 6)

        plt.title(r"z-score distribution for $\theta =$ %s"%(theta) )

        plt.savefig(out_directory + "ksn_zscore_%s.png" %(theta), dpi = 500)
        plt.clf()

def BandW_litho_z_score_global(df):
    """
        Print a box and whisker figure with ksn in function of lithologies for each concavity indexes
        
    """
    # check if a directory exists for the chi plots. If not then make it.
    out_directory = './sensitivity_concav/'

    if not os.path.isdir(out_directory):
        print("I am creating the river_plot/ directory to save your figures")
        os.makedirs(out_directory)


    fig = plt.figure(1, facecolor = "white", figsize=(14,8))

    gs = plt.GridSpec(1,8,bottom=0.15,left=0.08,right=0.97,top=0.95)

    tax = []
    for i in range(8):
        #tax.append(fig.add_subplot(gs[0,i], facecolor = "None"))
        tax.append(fig.add_subplot(gs[0,i]))
        
    data_to_plot_glob = []
    name_global = []
    xlab = []    
    BoxColor=['#9D78C1','#6E899B','#F3C793','#B1DEDE','#C8C864','#A6835F','#AF5A5A','#A7DBA7']

    for geol in df["Classification"].unique(): 

        tdf = df[df["Classification"] == geol]

        data_to_plot = []
        names = []
        even = 1
        for theta in tdf["concavity_index"].unique():
            tdf2 = tdf["z_score_glob"][tdf["concavity_index"] == theta]
            data_to_plot.append(tdf2)
            if even % 2 ==0:
                names.append(theta)

            else:

                names.append("\n" + str(theta))
            even += 1

        data_to_plot_glob.append(data_to_plot)
        name_global.append(names)
        xlab.append(geol)
        #print geol


    for i in range(8):

        bp = tax[i].boxplot(data_to_plot_glob[i], labels = name_global[i], patch_artist = True, showfliers = False)
        #bp = tax[i].boxplot(data_to_plot_glob[i], patch_artist = True)

        ## change outline color, fill color and linewidth of the boxes
        for box in bp['boxes']:
            # change outline color
            box.set( color='k', linewidth=0.5)
            # change fill color
            box.set( facecolor = BoxColor[i] )

        ## change color and linewidth of the whiskers
        for whisker in bp['whiskers']:
            whisker.set(color = 'k', linewidth=0.5)

        ## change color and linewidth of the caps
        for cap in bp['caps']:
            cap.set(color='#2C2C2C', linewidth=0.25)

        ## change color and linewidth of the medians
        for median in bp['medians']:
            median.set(color='#A54747', linewidth=0.5)

        ## change the style of fliers and their fill
        for flier in bp['fliers']:
            flier.set(marker='+', color='#A0A0A0', alpha=0.5)

        tax[i].tick_params(axis = "x", width = 0.05, length = 0.05, labelsize = 3)
        tax[i].set_xlabel(xlab[i], fontsize = 6)
        tax[i].set_ylim(-4.2,4.2)
        tax[i].grid(ls = '-', dashes=(5, 2.5), lw = 0.2, c = "k")

        if(i > 0):
            tax[i].yaxis.set_ticks_position("none")
            tax[i].set_ylabel("")
            tax[i].set_yticklabels("")
        else:
            tax[i].set_ylabel(r"$k_{sn}$ z-score per $\theta$", fontsize = 8)
            tax[i].tick_params(axis = "y", labelsize = 6)


    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.05, hspace=None)
    plt.savefig(out_directory + "ksn_zscore_global.png", dpi = 1200)
    plt.savefig(out_directory + "ksn_zscore_global.pdf", dpi = 1200)
    plt.clf()


# def plot_spatial_sensitivity_1(df, n_perc_bin = 10, conc =[0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6]):
#     """
#         This is the second sensitivity analysis about the ksn - concavity index
#     """

#     out_directory = './sensitivity_concav/'

#     if not os.path.isdir(out_directory):
#         print("I am creating the river_plot/ directory to save your figures")
#         os.makedirs(out_directory)

#     fig = plt.figure(1, facecolor = "white", figsize=(5,5))

#     gs = plt.GridSpec(100,100,bottom=0.15,left=0.15,right=0.95,top=0.95)

#     ax1 = fig.add_subplot(gs[0:100,0:100], facecolor = "None")

#     n_tim_in_same_percentile = {}
#     for i in range(1,12):
#         n_tim_in_same_percentile[i] = 0

#     for node in df["node"].unique():
#         tdf = df[df["node"] == node]
#         # print("node %s: %s" %(node, tdf.shape[0]))
#         n_thind = tdf["percentile"].unique()
#         print(n_thind)
#         n_tim_in_same_percentile[n_thind.shape[0]] += 1


#     for key in n_tim_in_same_percentile:
#         data = n_tim_in_same_percentile[key]
#         ax1.scatter(key,data, s = 2, marker = "s", c = "k")


#     ax1.set_xlabel("number of percentiles a node is present")
#     ax1.set_ylabel("number of nodes")


#     plt.savefig(out_directory + "ksn_stat_var.png", dpi = 500)
#     plt.clf()

# def plot_spatial_sensitivity_2(df, n_perc_bin = 10, conc =[0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6]):
#     """
#         This is the second sensitivity analysis about the ksn - concavity index
#     """

#     out_directory = './sensitivity_concav/'

#     if not os.path.isdir(out_directory):
#         print("I am creating the river_plot/ directory to save your figures")
#         os.makedirs(out_directory)

#     fig = plt.figure(1, facecolor = "white", figsize=(5,5))

#     gs = plt.GridSpec(100,100,bottom=0.15,left=0.15,right=0.95,top=0.95)

#     ax1 = fig.add_subplot(gs[0:100,0:100], facecolor = "None")
#     n_tim_in_same_percentile =[]
#     nn = df["node"].unique().shape[0]
#     indent = 0
#     for node in df["node"].unique():
#         tdf = df[df["node"] == node]
#         # print("node %s: %s" %(indent, nn))
#         n_thind = tdf["percentile"].unique()
#         ranger = n_thind.max() - n_thind.min()
#         print("%s,%s" %(n_thind.max(),n_thind.min()))
#         n_tim_in_same_percentile.append(ranger)
#         indent +=1

#     ax1.hist(n_tim_in_same_percentile,bins = 100, lw =3 )


#     ax1.set_xlabel("range of percentiles for each nodes")
#     ax1.set_ylabel("number of nodes")


#     plt.savefig(out_directory + "ksn_stat_var_range.png", dpi = 500)
#     plt.clf()





if __name__ == "__main__":


    # Loading the dataframes , concatenating it and adding two columns: "concavity_index" and "z_score_global"
    #df = load_the_dataframe(path = "/home/s1687599/Datastore/LSDTopoTools/Topographic_projects/LSDTT_Pyrenees_data/m_over_n_analyses/PYRENEES/sensitivity_test_movern/",common_name_of_csv_with_geology = "Extract_Basin_PYRENEES_Geology.csv", conc =[0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70])
    # Group the geology and add a column "Classification" with the global name below
    #df = group_geologies(df, dictionnary_of_litho = {"Plutonic r.": [4,7,9], "Metamorphic r.":[5], "Volcanic r.": [3,6], "Mixed s.r.": [2], "Carbonate s.r.": [10], "Siliciclastic s.r.": [8], "Unconsolidated s.r.": [1], "Water Body": [11]})
    # Save the csv. 
    #df.to_csv("complete_csv.csv", index = False) # Index = False prevent the creation of a useless column
    # Once you've done that (and as long as you don't rerun the code) you can comment the previous lines and just use:
    #df = pd.read_csv("complete_csv.csv")

    # big figure
    BandW_litho_z_score_global(df)







