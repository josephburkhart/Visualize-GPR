# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:11:11 2021

@author: Joseph

Functions for visualizing GPR using Pyvista and numpy
"""
import pyvista as pv

def surface_values():
    """Ask the user for threshold values which will be used to create isosurfaces."""
    values = []  #list for input values
    prompt = 'Enter desired isosurface values singly or as a comma-separated list. If there are no more values, enter \'done\' '
    
    while True:
        inputs = input(prompt)  #get user inputs
        
        if inputs == 'done':    #break loop if user is done
            print(f'\nDone! Your isosurface values are {values}')
            break 
        
        inputs_as_floats = [float(i) for i in inputs.split(sep=',')]
        values.extend(inputs_as_floats)  #add input values into list
        
    return values

def create_surface(value, mesh, p):
    """
    Create isosurface for given threshold value (callback for pyvista's slider bar widget)
    
    mesh must be a pyvista.RectilinearGrid() object
    p must be a pyvista.Plotter(notebook=False) object                                 
    """
    threshold = int(value)
    contours = mesh.contour(isosurfaces=[threshold])
    p.add_mesh(contours, opacity=1.0, color='white', name='contours')
    return

def export_surface(mesh, value: float, projectname: str):
    """Using pyvista, create a mesh and export it in OBJ format"""    
    filename = projectname + '_isosurface' + str(round(value)) + '.obj'
    surface = mesh.contour(isosurfaces=[value])
    pv.save_meshio(filename, surface)
    return
