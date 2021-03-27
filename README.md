# Visualize GPR
These are some scripts for working with 3D GPR data using vtk isosurfaces in Python. The user can interactively visualize the data, save 3D models of the surfaces in OBJ format, and save animations of the surfaces as MP4 videos.
 
These scripts are only compatible with 3D GPR data stored in [Hierarchical Data Format 5](https://support.hdfgroup.org/HDF5/) (HDF5, .h5). More data formats may be added in the future. If your data is not in HDF5, see some helpful conversion tools can be found [here](https://support.hdfgroup.org/products/hdf5_tools/toolsbycat.html). If your data is in an older HDF format (.hdf), tools for converting it to HDF5 can be found [here](https://support.hdfgroup.org/products/hdf5_tools/h4toh5/).

## Requirements
- Python (3.7 or newer)
- pyvista
- numpy
- h5py

## Setup
1. Clone this repository
2. Install the required packages (see above)
    - Note: recommended install using anaconda - see [here](https://docs.anaconda.com/anaconda/install/) for instructions on setting up anaconda
3. In `hdf5-to-obj.py`, set the name variables according to your data:
    - set `datafile_name` to the name of your data file
    - set `project_name` to the name of your project (this will be appended to the file names of your models)
    - set `dname` to the name of the 3D dataset in your data file. If you do not know this information, you can determine it using the [HDFView Tool](https://www.hdfgroup.org/downloads/hdfview/).
    - set `xname`, `yname`, and `zname` to the names of the x, y, and z arrays in your data file
4. In `make-movie.py`, set the name variables according to your data:
    - set `datafile_name` to the name of your data file
    - set `movie_name` to the name you want for your movie file
    - set `dname`, `xname`, `yname`, and `zname` as above
5. Move your data file into the repository

The script files are now ready to use. Follow the prompts in the console.
