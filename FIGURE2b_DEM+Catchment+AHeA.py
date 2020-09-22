"""
Created on Tue Feb 20 16:51:05 2018
@author: Thomas B (Python 3.6)
Description:
"""

#%%===============================IMPORT_LIBRARY============================%%#
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import time as clock
from matplotlib import rcParams
import matplotlib.cm as cm
import LSDPlottingTools as LSDP
from LSDMapFigure.PlottingRaster import MapFigure
from LSDMapFigure.PlottingRaster import BaseRaster
from LSDPlottingTools import colours as lsdcolours
from LSDPlottingTools import init_plotting_DV
import sys
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, DrawingArea, HPacker
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
import matplotlib.lines as mlines
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

#%%=============================FILES_PARAMETERS============================%%#
Import_Directory='/home/s1687599/Datastore/LSDTopoTools/Topographic_projects/LSDTT_Pyrenees_data/Basin_Analyses_v5_LSDTT/'
Export_Directory = '/home/s1687599/Datastore/Post-orogenic sediment flux to continental margins/Publication_Report/Paper_Control_of_lithology_on_landscape_of_the post-orogenesis_of_Pyrenees_TB-HS/FIGURE_V2.0/' 
ExportFigure = Export_Directory+'FIGURE1b_Pyrenees_DEM+Catchment+AFTA.pdf'

BaseRasterName='Pyrenees_v5_PP_Zoom.bil'
HSRaster='Pyrenees_v5_PP_hs_Zoom.bil'
BasinInfoPrefix_NogPal = 'Extract_Basin_NogueraPallaresa'
RasterName_NogPal = 'Extract_Basin_NogueraPallaresa_AllBasins.bil'
BasinInfoPrefix_NogRib = 'Extract_Basin_NogueraRibagorzana'
RasterName_NogRib = 'Extract_Basin_NogueraRibagorzana_AllBasins.bil'
BasinInfoPrefix_Ira = 'Extract_Basin_Irati2'
RasterName_Ira = 'Extract_Basin_Irati2_AllBasins.bil'
BasinInfoPrefix_LLo = 'Extract_Basin_Llobegrat'
RasterName_LLo = 'Extract_Basin_Llobegrat_AllBasins.bil'
BasinInfoPrefix_GdP = 'Extract_Basin_GavedePau'
RasterName_GdP = 'Extract_Basin_GavedePau_AllBasins.bil'
BasinInfoPrefix_Gar = 'Extract_Basin_Garonne2'
RasterName_Gar = 'Extract_Basin_Garonne2_AllBasins.bil'
BasinInfoPrefix_Gal = 'Extract_Basin_Gallego'
RasterName_Gal = 'Extract_Basin_Gallego_AllBasins.bil'
BasinInfoPrefix_Cin = 'Extract_Basin_Cinca'
RasterName_Cin = 'Extract_Basin_Cinca_AllBasins.bil'
BasinInfoPrefix_Aud = 'Extract_Basin_Aude'
RasterName_Aud = 'Extract_Basin_Aude_AllBasins.bil'
BasinInfoPrefix_Ari = 'Extract_Basin_Ariege'
RasterName_Ari = 'Extract_Basin_Ariege_AllBasins.bil'
BasinInfoPrefix_Ara = 'Extract_Basin_Aragon2'
RasterName_Ara = 'Extract_Basin_Aragon2_AllBasins.bil'
BasinInfoPrefix_Tet = 'Extract_Basin_Tet'
RasterName_Tet = 'Extract_Basin_Tet_AllBasins.bil'
BasinInfoPrefix_Ter = 'Extract_Basin_Ter'
RasterName_Ter = 'Extract_Basin_Ter_AllBasins.bil'
BasinInfoPrefix_Seg = 'Extract_Basin_Segre'
RasterName_Seg = 'Extract_Basin_Segre_AllBasins.bil'
BasinInfoPrefix_Sal = 'Extract_Basin_Salat2'
RasterName_Sal = 'Extract_Basin_Salat2_AllBasins.bil'
BasinInfoPrefix_Sai = 'Extract_Basin_Saison'
RasterName_Sai = 'Extract_Basin_Saison_AllBasins.bil'

csv_file1 = Import_Directory+'AHe_Data_used.csv'
csv_file2 = Import_Directory+'AHe_Data_not_used.csv'

#%%============================LOAD_AND_PLOT_DATA===========================%%#
plt.clf() 
MF = MapFigure(BaseRasterName=BaseRasterName,
               Directory=Import_Directory,
               coord_type="UTM",
               colourbar_location="None",
               basemap_colourmap="gray",
               plot_title='None',
               NFF_opti=False,alpha=1,zorder=1)

MF.add_drape_image(RasterName=HSRaster,Directory=Import_Directory,
                   colourmap = "gray",
                   alpha=0.25,
                   colorbarlabel = "Colourbar", discrete_cmap=False,
                   n_colours=10, norm = "None",
                   colour_min_max = [],
                   modify_raster_values = False,
                   old_values=[], new_values = [], cbar_type=float,
                   NFF_opti = False, custom_min_max = [],zorder=2)

MF.add_basin_plot(RasterName=RasterName_NogPal,BasinInfoPrefix=BasinInfoPrefix_NogPal,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'13'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_NogRib,BasinInfoPrefix=BasinInfoPrefix_NogRib,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'12'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Ira,BasinInfoPrefix=BasinInfoPrefix_Ira,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'8'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_LLo,BasinInfoPrefix=BasinInfoPrefix_LLo,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'15'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_GdP,BasinInfoPrefix=BasinInfoPrefix_GdP,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'2'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Gar,BasinInfoPrefix=BasinInfoPrefix_Gar,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'3'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Gal,BasinInfoPrefix=BasinInfoPrefix_Gal,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'10'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Cin,BasinInfoPrefix=BasinInfoPrefix_Cin,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'11'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Aud,BasinInfoPrefix=BasinInfoPrefix_Aud,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'6'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Ari,BasinInfoPrefix=BasinInfoPrefix_Ari,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'5'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Ara,BasinInfoPrefix=BasinInfoPrefix_Ara,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'9'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Tet,BasinInfoPrefix=BasinInfoPrefix_Tet,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'7'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Ter,BasinInfoPrefix=BasinInfoPrefix_Ter,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'16'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Seg,BasinInfoPrefix=BasinInfoPrefix_Seg,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'14'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Sal,BasinInfoPrefix=BasinInfoPrefix_Sal,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'4'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Sai,BasinInfoPrefix=BasinInfoPrefix_Sai,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = "False", colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'1'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)

thisPointData1=LSDP.LSDMap_PointData(csv_file1, PANDEX=True)
thisPointData2=LSDP.LSDMap_PointData(csv_file2, PANDEX=True)
MF.add_point_data(thisPointData=thisPointData1,
                  column_for_plotting='age',
                  this_colourmap="hot_r",
                  show_colourbar=True,
                  colourbar_location='right',
                  colorbarlabel='Apatite helium age',
                  scale_points=False, column_for_scaling='age',                  
                  scaled_data_in_log=False,                  
                  max_point_size=10, min_point_size=0,
                  colour_log=False,
                  colour_manual_scale=[0,70],
                  manual_size=20,
                  alpha=1,marker=(4,0,0),
                  zorder=4)
MF.add_point_data(thisPointData=thisPointData2,
                  column_for_plotting='age',
                  this_colourmap="hot_r",
                  show_colourbar=False,
                  colourbar_location='right',
                  colorbarlabel='Apatite helium age',
                  scale_points=False, column_for_scaling='age',                  
                  scaled_data_in_log=False,                  
                  max_point_size=10, min_point_size=0,
                  colour_log=False,
                  colour_manual_scale=[0,70],
                  manual_size=20,
                  alpha=1,marker='o',
                  zorder=4)

#%%==================================Legend=================================%%#
#fig = matplotlib.pyplot.gcf()
#gs = plt.GridSpec(100,100,bottom=0,left=0,right=1,top=1)
#ax_off = fig.add_subplot(gs[0:100,0:100])
#
#star=mlines.Line2D([],[],color='red',marker='*',mec='k',linestyle='None',markersize=12,label='AFT used in this study')
#circle=mlines.Line2D([],[],color='red',marker='o',mec='k',linestyle='None',markersize=10,label='AFT Available')
#
#ax_off.legend(handles=[circle,star],fontsize=8,labelspacing=0.2,handletextpad=0.25,borderpad=0.1,loc=3,facecolor=(0.773,0.898,0.961),fancybox=True,edgecolor=(0,0,0,1))
#
#ax_off.patch.set_alpha(0)
#ax_off.patch.set_visible(False)
#ax_off.axis('off')

#%%====================================TEST=================================%%#
boxc1=TextArea(' AHeA available:\n AHeA used for the study:',textprops=dict(color='k',fontsize=9))
Boxc2=DrawingArea(12.5,20)
Recc0= Rectangle((5,0),width=6,height=6,angle=45,fc='darkred',ec='darkred')
Recc1= Circle((5,15),radius=3.5,fc='darkred',ec='darkred')

Boxc2.add_artist(Recc0)
Boxc2.add_artist(Recc1)

boxc = HPacker(children=[boxc1,Boxc2],align="center",pad=3,sep=2.5)

anchored_boxc=AnchoredOffsetbox(loc=3,child=boxc,pad=0,frameon=True,borderpad=0)
5
fig = matplotlib.pyplot.gcf()
gs = plt.GridSpec(100,100,bottom=0.23249,left=0.14166,right=0.70833,top=0.69596)
ax_off = fig.add_subplot(gs[0:100,0:100])

ax_off.add_artist(anchored_boxc) 

ax_off.patch.set_alpha(0)
ax_off.patch.set_visible(False)
ax_off.axis('off')

#%%================================FIGURE_SAVE==============================%%#
#MF.show_plot()

MF.save_fig(fig_width_inches=6,
            FigFileName=ExportFigure,
            FigFormat='pdf',
            Fig_dpi=1200) #save the export figure
