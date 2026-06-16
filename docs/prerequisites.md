# Prerequisites

## Earthdata Login

A NASA Earthdata Login (EDL) account is required to access data, as well as discover restricted data, from the NASA Earthdata system. 

Please visit https://urs.earthdata.nasa.gov to register and manage your Earthdata Login account. This account is free to create and only takes a moment to set up. The Earthdata Login provides a single mechanism for user registration and profile management for all NASA EOSDIS system components (DAACs, tools, and services).

Please refer to this page for more info about [how to register to the EDL](https://urs.earthdata.nasa.gov/documentation/what_do_i_need_to_know). 

## Python Modules
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

## Compute Environment

These tutorials can be run in any personal computing environment (e.g., desktop/laptops), on-premise solution (e.g., High-Performance Computing), or on the Cloud (e.g., Amazon Web Service).

The tutorials use [JupyterLab](https://jupyter.org/) to run the scripts and print the results. JupyterLab is a web-based interactive development environment for notebooks, code, and data. 

To install Jupyterlab with `pip`, run the following on the terminal:
```bash 
pip install jupyterlab
```

Once installed, type the following in your terminal: 
```bash
jupyter lab
```

The Jupyter notebooks can also be launched to external environments like Google's [Colab](https://colab.research.google.com/), [MyBinder](https://mybinder.org/) or other managed cloud environment like [NASA Openscape 2i2c](https://openscapes.2i2c.cloud/).

You can also [clone this repository](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-use-external.html#studio-lab-use-external-clone-github) to the [Amazon Sagemaker Studio Lab](https://studiolab.sagemaker.aws/), which is a free computing environment on the AWS cloud.

## GitHub Account

You will need a [GitHub](https://github.com) account to contribute to this repository via pull requests or to access a JupyterHub environment such as [NASA Openscape's 2i2c](https://openscapes.2i2c.cloud).

This [document](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github#signing-up-for-a-new-personal-account) will guide you through the steps of signing up for a free personal GitHub account.

### Git
Once you have a GitHub account, it is important to understand fundamental `Git` concepts. Familiarize yourself with `Git` by referring to this [introductory guide](https://docs.github.com/en/get-started/getting-started-with-git) and [this handy cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf).

[This installation guide](https://github.com/git-guides/install-git) provides instructions on how to install `Git` in your system (Windows, Linux, or Mac) if it is not already installed. 

### GitHub Authentication
There are several ways to authenticate your GitHub account. We will use a [SSH authentication method](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

1. Generate a new SSH key: Open your terminal (or Git Bash on Windows) and run the following command: 
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
2. Copy the SSH key:  Copy the contents of your SSH key file, located at `~/.ssh/id_ed25519.pub`, to your clipboard. 
3. Add the SSH Key to GitHub: Navigate to https://github.com/settings/keys on your GitHub and click the "New SSH Key" button. Provide a title for your key and paste the contents you copied in Step 2 into the key field. Click "Add SSH Key" to save.

You are now set up to use SSH for connecting to GitHub.

### Git Clone

To get started, clone this [GEDI data tutorials](https://github.com/ornldaac/gedi_tutorials) git repository by running the following command on your terminal (or Git bash in Windows):

```bash
git clone git@github.com:ornldaac/gedi_tutorials.git
```