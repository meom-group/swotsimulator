# -----------------------#
# Files and directories
# -----------------------#

# ------ Directory that contains orbit file:
dir_setup='[yourpath]/SWOT_simulator/data/'
# ------ Directory that contains your own inputs:
indatadir='[yourpath_to_yourdata]/'
# ------ Directory that contains your outputs:
outdatadir='[yourpath_to_outputs]/'
# ------ Orbit file:
satname=[yoursatname]
filesat=[dir_setup+'/orbit[sat1].txt', dir_setup+'/orbit[sat2].txt', ...]
# ------ Name of the configuration (to build output files names) 
config='[nameofyourconfig]'

# -----------------------#
# NADIR orbit parameters
# -----------------------#

# ------ Satellite grid file root name:
#        (Final file name is root_name_p[numberofpass].nc)
filesgrid=outdatadir+'/'+config+'_'+satname+'_grid'
or filesgrid=outdatadir+'/'+'[your_grid_root_name]'
# ------ Force the computation of the satellite grid:
makesgrid=True or False
# ------ Give a subdomain if only part of the model is needed:
#        (modelbox=[lon_min, lon_max, lat_min, lat_max])
#        (If modelbox is None, the whole domain of the model is considered)
modelbox=None or [yourlon_min, yourlon_max, yourlat_min, yourlat_max]
# ------ Distance between the nadir and the end of the swath (in km):
halfswath=60.
# ------ Distance between the nadir and the beginning of the swath (in km):
halfgap=10.
# ------ Along track resolution (in km):
delta_al=6.
# ------ Shift longitude of the orbit file if no pass is in the domain (in degree):
#        Default value is None (no shift)
shift_lon=None
# ------ Shift time of the satellite pass (in day):
#        Default value is None (no shift)
shift_time=None

# -----------------------#
# Model input parameters
# -----------------------#
# ------ List of model files:
#        (The first file contains the grid and is not considered as model data)
#        To generate the noise alone, file_input=None and specify region in modelbox
file_input=indatadir+'/[your_list_of_file_name.txt]' or None
# ------ Type of model data:
#        (Optional, default is NETCDF_MODEL and reads netcdf3 and netcdf4 files)
model='NETCDF_MODEL'
# ------ Type of grid: 
# 'regular' or 'irregular', if 'regular' only 1d coordinates are extracted from model       
grid='irregular'
# ------ Specify SSH variable:
var='H'
# ------ Specify factor to convert SSH values in m:
SSH_factor=1.
# ------ Specify longitude variable:
lon='lon_rho'
# ------ Specify latitude variable:
lat='lat_rho'
# ------ Time step between two model outputs (in days):
timestep=1.
# ------ Number of outputs to consider:
#        (timestep*nstep=total number of days)
nstep=50.
# ------ Not a number value:
model_nan=0.

# -----------------------# 
# NADIR output files  
# -----------------------# 
# ------ Output file root name:
#        (Final file name is root_name_c[cycle]_p[pass].nc
file_output=outdatadir+'/'+config+'_'+satname
or file_output=outdatadir+'/[your_output_root_name]'
# ------ Interpolation of the SSH from the model (if grid is irregular and 
#         pyresample is not installed:
#        (either 'linear' or 'nearest', use 'nearest' for large region
#        as it is faster and use less memory)
interpolation='nearest' or ‘linear’

# -----------------------#
# NADIR error parameters
# -----------------------#
# ------ File containing random coefficients to compute and save
#        random error coefficients so that runs are reproducible:
#        If file_coeff is specified and does not exist, file is created
#        If you don't want runs to be reproducible, file_coeff is set to None
file_coeff=outdatadir+'/Random_coeff.nc'
# ------ Numbers of random realisations for instrumental and geophysical error (recommended ncomp=2000), ncomp1d is used for 1D spectrum, and ncomp2d is used for 2D spectrum (wet troposphere computation):
ncomp1d=3000
ncomp2d=2000

## -- Geophysical error
## ----------------------
# ------ Wet tropo error (True to compute it):
wet_tropo=True or False
# ------ Beam print size (in km):
#        Gaussian footprint of sigma km
sigma=8.
# ------ Across track resolution of the beam for the correction of the wet tropo (in km):
delta_ac=6.
