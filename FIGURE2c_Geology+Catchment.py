"""
Created on Fri Feb 23 14:28:42 2018
@author: Thomas B
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
Import_Directory = '/home/s1687599/Datastore/LSDTopoTools/Topographic_projects/LSDTT_Pyrenees_data/Basin_Analyses_v5_LSDTT/' # reading directory (if it is on windows, the path is something like C://windows/Users/blablalba/)
BaseRasterName = 'Pyrenees_v5_PP_hs_Zoom.bil' # It will be the cabkground raster. Each other raster you want to drap on it will be cropped to its extents including nodata
Export_Directory = '/home/s1687599/Datastore/Post-orogenic sediment flux to continental margins/Publication_Report/Paper_Control_of_lithology_on_landscape_of_the post-orogenesis_of_Pyrenees_TB-HS/FIGURE_V2.0/' # writing directory (if it is on windows, the path is something like C://windows/Users/blablalba/)
ExportFigure = Export_Directory+'FIGURE1c_Geology+Catchment.pdf'
RasterName = "Pyrenees_v5_PP_Zoom_Geology.bil" # if you want to drap a raster on your background one. Just add a similar line in case you want another raster to drap and so on

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

#%%========================CUSTOM_SEGMENTED_COLORMAP========================%%#
CustomColor=['#C8C864','#AF5A5A','#A7DBA7','#F3C793','#F5A7A7','#6E899B','#A6835F','#9D78C1','#6E9C6E','#DAB0DA','#B1DEDE']
CustomColorMap = matplotlib.colors.ListedColormap(CustomColor)

CustomColorComb=['#C8C864','#AF5A5A','#A7DBA7','#F3C793','#AF5A5A','#6E899B','#A6835F','#9D78C1','#6E9C6E','#AF5A5A','#B1DEDE']
CustomColorCombMap = matplotlib.colors.ListedColormap(CustomColorComb)

CustomColorCombForLegend=['#C8C864','#AF5A5A','#A7DBA7','#F3C793','#6E899B','#A6835F','#9D78C1','#6E9C6E','#B1DEDE']
CustomColorCombForLegendMap = matplotlib.colors.ListedColormap(CustomColorCombForLegend)

#%%============================LOAD_AND_PLOT_DATA===========================%%#
plt.clf() 

MF = MapFigure(BaseRasterName=BaseRasterName,
               Directory=Import_Directory,
               coord_type="UTM",
               colourbar_location="right",
               basemap_colourmap="gray",
               plot_title='None',
               NFF_opti=False) # load and display the background hillslope raster

MF.add_drape_image(RasterName=RasterName,
                   Directory=Import_Directory,
                   colourmap=CustomColorCombMap,
                   alpha=0.66,
                   show_colourbar=False,
                   colorbarlabel='Lithology',
                   modify_raster_values=False,
                   NFF_opti=False)

MF.add_basin_plot(RasterName=RasterName_NogPal,BasinInfoPrefix=BasinInfoPrefix_NogPal,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'13'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_NogRib,BasinInfoPrefix=BasinInfoPrefix_NogRib,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'12'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Ira,BasinInfoPrefix=BasinInfoPrefix_Ira,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'8'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_LLo,BasinInfoPrefix=BasinInfoPrefix_LLo,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'15'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_GdP,BasinInfoPrefix=BasinInfoPrefix_GdP,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'2'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Gar,BasinInfoPrefix=BasinInfoPrefix_Gar,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'3'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Gal,BasinInfoPrefix=BasinInfoPrefix_Gal,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'10'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Cin,BasinInfoPrefix=BasinInfoPrefix_Cin,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'11'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Aud,BasinInfoPrefix=BasinInfoPrefix_Aud,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'6'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Ari,BasinInfoPrefix=BasinInfoPrefix_Ari,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'5'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Ara,BasinInfoPrefix=BasinInfoPrefix_Ara,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'9'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Tet,BasinInfoPrefix=BasinInfoPrefix_Tet,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'7'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Ter,BasinInfoPrefix=BasinInfoPrefix_Ter,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'16'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Seg,BasinInfoPrefix=BasinInfoPrefix_Seg,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'14'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Sal,BasinInfoPrefix=BasinInfoPrefix_Sal,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'4'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)
MF.add_basin_plot(RasterName=RasterName_Sai,BasinInfoPrefix=BasinInfoPrefix_Sai,Directory=Import_Directory,
                 colourmap = "gray",alpha=0.2,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = True, adjust_text = False, rename_dict = {0:'1'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=1, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3)

#%%================================FIGURE_SAVE==============================%%#
MF.save_fig(fig_width_inches=6,
            FigFileName=ExportFigure,
            FigFormat='pdf',
            Fig_dpi=1200) 