# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 14:38:23 2020

@author: Joseph

This script imports a 3D gridded dataset from hdf5, asks the user for their chosen isosurface values,
creates an isosurface for each value, and then exports each isosurface in OBJ format.

What the final script may eventually do:
    process the hdf, turn it into a vtr?
    make an interactive rendering of the data with a slider bar
    extract surfaces on the basis of input from the slider bar
    accept multiple inputs from the slider bar and save the resulting surfaces as obj files 
"""

import numpy as np
import pyvista as pv
import h5py
import vizgpr as vz
from functools import *

# Names
data_name = 'BLDG_16_3D.h5'
project_name = 'KAD_gpr_Building16'

# Import data
f = h5py.File(data_name, 'r')

data = np.array(f['BLDG_16_3D'], dtype=np.float64) #when batch processing, keys will need to be defined implicitly

xdim = np.array(f['DimY'], dtype=np.float64)       #not a typo - DimY is assigned to xdim because the data was improperly rotated
ydim = np.array(f['DimX'], dtype=np.float64)       #not a typo - DimX is assigned to ydim because the data was improperly rotated
zdim = np.array(f['DimZ'], dtype=np.float64)


# Wrap data in pyvista rectilinear grid object
mesh = pv.RectilinearGrid()

mesh.x = xdim   #add the coordinates
mesh.y = ydim
mesh.z = zdim    

mesh.point_arrays['gpr'] = data.flatten(order='F')    # Add the data values to the cell data (https://docs.pyvista.org/examples/00-load/create-uniform-grid.html#sphx-glr-examples-00-load-create-uniform-grid-py)

mesh.set_active_scalars('gpr')    #probably not necessary, but here just in case
    

# Plot (user must exit the plotter window in order to move on to the next section - hit 'q' to do this)
print("Initializing plotter, hit q to continue")
p = pv.Plotter(notebook=False)

widget_callback = partial(vz.create_surface, mesh=mesh, p=p)
p.add_mesh(mesh.outline(), color="k")
p.camera_position = [0,0,100]
p.add_slider_widget(widget_callback, 
                    rng=[np.amin(data), np.amax(data)], 
                    title='Isosurface Threshold')
p.show()


# Make isosurfaces and export them
for value in vz.surface_values():
    vz.export_surface(mesh=mesh, value=value, projectname=project_name)
 

