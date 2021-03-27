# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 14:38:23 2020

@author: Joseph

This script imports a 3D gridded dataset from hdf5, asks the user for their chosen isosurface values,
creates an isosurface for each value, and then exports each isosurface in OBJ format.

This version is specifically for making a movie for Kevin Fisher

What the final script may eventually do:
    process the hdf, turn it into a vtr?
    make an interactive rendering of the data with a slider bar
    extract surfaces on the basis of input from the slider bar
    accept multiple inputs from the slider bar and save the resulting surfaces as obj files 
"""

import numpy as np
import h5py
import math as m
import pyvista as pv

# Filenames
data_name = 'BLDG_16_3D.h5'
movie_name = 'KAD_GPR_BLDG16_500to6000per50.mp4'

# Import data
f = h5py.File(data_name, 'r')

data = np.array(f['BLDG_16_3D'], dtype=np.float64) #when batch processing, keys will need to be defined implicitly

xdim = np.array(f['DimY'], dtype=np.float64)       #why does it need to be DimY to work, instead of DimX?
ydim = np.array(f['DimX'], dtype=np.float64)       #why does it need to be DimX to work, instead of DimY?
zdim = np.array(f['DimZ'], dtype=np.float64)


# Wrap data in pyvista rectilinear grid object
mesh = pv.RectilinearGrid()

mesh.x = xdim   #add the coordinates
mesh.y = ydim
mesh.z = zdim    

mesh.point_arrays['gpr'] = data.flatten(order='F')    # Add the data values to the cell data (https://docs.pyvista.org/examples/00-load/create-uniform-grid.html#sphx-glr-examples-00-load-create-uniform-grid-py)

mesh.set_active_scalars('gpr')    #probably not necessary, but here just in case


# Make a compass
arrow_start = np.array([25,-4,0])
north_arrow = pv.Arrow(start=arrow_start, direction=[-1,0,0], scale=8)
cross_bar = pv.Cylinder(center=[22,-4,0], direction=[0,-3,0], height=6, radius=0.4)

# Plot
p = pv.Plotter(notebook=False)
p.add_mesh(mesh.outline(), color="k")

p.add_mesh(north_arrow, color='red', show_edges=False)
p.add_mesh(cross_bar, color='red', show_edges=False)

p.camera_position = [0,0,20]
p.open_movie(movie_name)

# Render and do NOT close
contours = mesh.contour(isosurfaces=[6000])
p.add_mesh(contours, opacity=1.0, color='white', name='contours')
p.add_text(text=f'gpr threshold: 6000', name='threshold_label', font_size=14)
p.show(auto_close=False)

# Write initial frame
#p.write_frame()

# Update surface on each frame - Surface update movie
for value in np.linspace(500, 6000, 111):
    threshold = int(value)
    contours = mesh.contour(isosurfaces=[threshold])
    p.add_mesh(contours, opacity=1.0, color='white', name='contours')
    p.add_text(text=f'gpr threshold: {threshold}', name='threshold_label', font_size=14)
    p.write_frame()
    
# Update surface on each frame - camera position update movie
# for theta in np.linspace(0, 360, 361):
#     p.camera_position = [100*m.cos(m.radians(theta)), 100*m.sin(m.radians(theta)), 100]
#     p.write_frame()

p.close()
