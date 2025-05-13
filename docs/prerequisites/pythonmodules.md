# Python Modules
The tutorials requires additional Python modules installed in your system. These are listed on the [requirements.txt](../../requirements.txt) file within the repository. You can install the modules using `pip` as:

```bash
pip install -r requirements.txt
```

If you use `conda` environment, you can create and activate the conda environment as 

```bash
conda env create -f environment.yml
conda activate airborne
```

The tutorials specifically uses [`earthaccess`](https://github.com/nsidc/earthaccess) python module. `earthaccess` is a python library to search for, and download or stream NASA Earth science data with just a few lines of code. `earthaccess` handles authentication with [NASA's Earthdata Login (EDL)](https://urs.earthdata.nasa.gov/), search using [NASA's CMR](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html) and cloud-access through [fsspec](https://github.com/fsspec/filesystem_spec).