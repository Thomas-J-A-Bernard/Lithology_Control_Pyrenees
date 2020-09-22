"""
@author: Boris
Modified by Thomas
Need Python version 2 to work
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
import matplotlib.lines as mlines

#%%=============================FILES_PARAMETERS============================%%#
Import_Directory = '/home/s1687599/Datastore/LSDTopoTools/Topographic_projects/LSDTT_Pyrenees_data/Figure_Hillslope_vs_Geology_vs_mChi/' # reading directory (if it is on windows, the path is something like C://windows/Users/blablalba/)
BaseRasterName = 'Extract_Basin_NogueraPallaresa_hs.bil' # It will be the cabkground raster. Each other raster you want to drap on it will be cropped to its extents including nodata
Export_Directory = '/home/s1687599/Datastore/Post-orogenic sediment flux to continental margins/Publication_Report/Paper_Control_of_lithology_on_landscape_of_the post-orogenesis_of_Pyrenees_TB-HS/FIGURE_V2.0/' # writing directory (if it is on windows, the path is something like C://windows/Users/blablalba/)
ExportFigure = Export_Directory+'Figure5c_NogueraPallaresa_Hs_vs_Geology.pdf'
RasterName = "Extract_Geology_NogueraPallaresa.bil" # if you want to drap a raster on your background one. Just add a similar line in case you want another raster to drap and so on
csv_file = Import_Directory+'Extract_Basin_NogueraPallaresa_MChiSegmented.csv' # Name of your point file, add a similar line with different name if you have more than one point file
BasinInfoPrefix = 'Extract_Basin_NogueraPallaresa'
RasterNameCatch = 'Extract_Basin_NogueraPallaresa_AllBasins.bil'

#%%========================CUSTOM_SEGMENTED_COLORMAP========================%%#
CustomColor=['#C8C864','#9D78C1','#6E9C6E','#AF5A5A','#A6835F','#A7DBA7','#DAB0DA','#F3C79B','#F5A7A7','#6E899B','#B1DEDE']
CustomColorMap = matplotlib.colors.ListedColormap(CustomColor)

CustomColorComb=['#C8C864','#9D78C1','#6E9C6E','#AF5A5A','#A6835F','#A7DBA7','#AF5A5A','#F3C79B','#AF5A5A','#6E899B','#B1DEDE']
CustomColorCombMap = matplotlib.colors.ListedColormap(CustomColorComb)

#%%======================CONVERT_CSV_FILE_TO_SHAPEFILES=====================%%#
thisPointData=LSDP.LSDMap_PointData(csv_file, PANDEX=True)

#%%============================LOAD_AND_PLOT_DATA===========================%%#

plt.clf() 

MF = MapFigure(BaseRasterName=BaseRasterName,
               Directory=Import_Directory,
               coord_type="UTM",
               colourbar_location="Top",
               basemap_colourmap="gray",
               plot_title='None',
               NFF_opti=False,alpha=1) # load and display the background hillslope raster

MF.add_drape_image(RasterName=RasterName,
                   Directory=Import_Directory,
                   colourmap=CustomColorCombMap,
                   alpha=0.6,
                   show_colourbar=True,
                   colorbarlabel='Lithology',
                   modify_raster_values=False,
                   NFF_opti=False)               
               
MF.add_basin_plot(RasterName=RasterNameCatch,BasinInfoPrefix=BasinInfoPrefix,Directory=Import_Directory,
                 colourmap = "gray",alpha=1,
                 show_colourbar = False, colorbarlabel = "Colourbar",
                 discrete_cmap=False, n_colours=10, cbar_type=float,
                 use_keys_not_junctions = True,
                 label_basins = False, adjust_text = False, rename_dict = {0:'13'},
                 value_dict = {}, mask_list = [],
                 edgecolour='black', linewidth=2, cbar_dict = {}, parallel=False,
                 outlines_only = True,zorder = 3) 
                                                                     



#%%================================FIGURE_SAVE==============================%%#
MF.save_fig(fig_width_inches=6,
            FigFileName=ExportFigure,
            FigFormat='pdf',
            Fig_dpi=1200) #save the export figure                 