#processes a multi-file datase
#to extract the first valid reflectance measurement for each geometry. 
#iterates through the data, identifying the first non-null entry for each geometry across all files, 
#and then selects those specific reflectance values. 

import xarray as xr
import numpy as np

def get_first_xr(ds_in):
    #array with geomtery x files
    arr = ds_in['index'].data
    
    #we want to find the first file where the geom is not null
    # Initialize an array to store the indices of the first non-null entry for each column
    file_ind = np.full(arr.shape[1], -1)  # Using -1 as a placeholder for no non-null values
    
    # Iterate over each column
    for col_idx in range(arr.shape[1]):
        # Get the column
        col = arr[:, col_idx]
        
        # Find the index of the first non-null entry
        non_null_indices = np.where(~np.isnan(col))[0]
        
        if non_null_indices.size > 0:
            file_ind[col_idx] = non_null_indices[0]
    
    #create a list form 0 to len first_non_null_indices
    geom_ind = list(range(len(file_ind)))
    
    file_ind = xr.DataArray(file_ind, dims=["index"])
    geom_ind = xr.DataArray(geom_ind, dims=["index"])
    
    ds = ds_in.reflectance.isel(file=file_ind, geometry=geom_ind)
    ds['index'] = ds['index'].astype(int)
    #convert to dataset
    ds = ds.to_dataset(name='reflectance')
    
    return ds