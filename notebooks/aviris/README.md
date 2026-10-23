# AVIRIS
![alt text](images/aviris.png)

The Airborne Visible InfraRed Imaging Spectrometer - Classic ([AVIRIS-C](https://aviris.jpl.nasa.gov/)), Next Generation ([AVIRIS-NG](https://avirisng.jpl.nasa.gov/)), 3rd Generation ([AVIRIS-3](https://www.earthdata.nasa.gov/data/instruments/aviris-3)), and 5th Generation ([AVIRIS-5](https://www.earthdata.nasa.gov/data/instruments/aviris-5)) are four Facility Instruments (FIs) that are part of NASA's Airborne Science Program (ASP) and the Jet Propulsion Laboratory's (JPL) Earth Science Airborne Program. 

Data from AVIRIS-C, AVIRIS-NG, AVIRIS-3, and AVIRIS-5 are applicable to a wide range of studies in the fields of terrestrial and coastal aquatic plant physiology, atmospheric and aerosol studies, environmental science, snow hydrology, geology, volcanology, oceanography, soil and land management, agriculture, and limnology.

AVIRIS datasets are available at https://www.earthdata.nasa.gov/data/projects/aviris.

## AVIRIS-C Datasets
The [AVIRIS-C](https://www.earthdata.nasa.gov/data/instruments/aviris-c) is an imaging spectrometer that delivers calibrated images of the upwelling spectral radiance in 224 contiguous spectral channels with wavelengths from 400 to 2500 nanometers (nm). 

| Dataset | DOI | Short Name | Concept ID |
|---|---|---|---|
| AVIRIS-Classic: L1B Calibrated Radiance | [10.3334/ORNLDAAC/2155](https://doi.org/10.3334/ORNLDAAC/2155) | AVIRIS-Classic_L1B_Radiance_2155 | C2714723060-ORNL_CLOUD |
| AVIRIS-Classic: L2 Calibrated Reflectance  | [10.3334/ORNLDAAC/2154](https://doi.org/10.3334/ORNLDAAC/2154) | AVIRIS-Classic_L2_Reflectance_2154 | C2711871294-ORNL_CLOUD |

## AVIRIS-NG Datasets
The [AVIRIS-NG](https://www.earthdata.nasa.gov/data/instruments/aviris-ng) is the successor to AVIRIS-Classic and provides high signal-to-noise ratio imaging spectroscopy measurements in 425 contiguous spectral channels with wavelengths in the solar reflected spectral range (380-2510 nm) with 5 nm sampling. The AVIRIS-NG started operation in 2014 and is expected to replace the AVIRIS-C instrument. 

| Dataset | DOI | Short Name | Concept ID |
|---|---|---|---|
| AVIRIS-NG L1B Calibrated Radiance | [10.3334/ORNLDAAC/2095](https://doi.org/10.3334/ORNLDAAC/2095) | AVIRIS-NG_L1B_radiance_2095 | C2662359874-ORNL_CLOUD |
| AVIRIS-NG L2 Surface Reflectance | [10.3334/ORNLDAAC/2110](https://doi.org/10.3334/ORNLDAAC/2110) | AVIRIS-NG_L2_Reflectance_2110 | C4076410273-ORNL_CLOUD |

## AVIRIS-3 Datasets
The [AVIRIS-3](https://www.earthdata.nasa.gov/data/instruments/aviris-3) is the third of the AVIRIS spectrometer FI series and has higher signal-to-noise ratio performance than AVIRIS-C or AVIRIS-NG. The core spectrometer of AVIRIS-3 is an optically fast, F/1.8 Dyson imaging spectrometer spanning a wide width (39.5-degree field of view). The AVIRIS-3 provides measurements in 285 contiguous spectral channels with wavelengths in the solar reflected spectral range (390-2500 nm) with 7.4 nm sampling. The AVIRIS-3 started operation in 2023. 

| Dataset | DOI | Short Name | Concept ID |
|---|---|---|---|
| AVIRIS-3 L1B Calibrated Radiance | [10.3334/ORNLDAAC/2356](https://doi.org/10.3334/ORNLDAAC/2356) | AV3_L1B_RDN_2356 | C3236537162-ORNL_CLOUD |
| AVIRIS-3 L2A Orthocorrected Surface Reflectance | [10.3334/ORNLDAAC/2357](https://doi.org/10.3334/ORNLDAAC/2357) | AV3_L2A_RFL_2357 | C3369603199-ORNL_CLOUD |
| AVIRIS-3 L2B Greenhouse Gas Enhancements | [10.3334/ORNLDAAC/2358](https://doi.org/10.3334/ORNLDAAC/2358) | AV3_L2B_GHG_2358 | C3236537512-ORNL_CLOUD |

## AVIRIS-5 Datasets

The [AVIRIS-5](https://www.earthdata.nasa.gov/data/instruments/aviris-5) is the latest version of NASA AVIRIS spectrometers, following AVIRIS-C, AVIRIS-NG, and AVIRIS-3. AVIRIS-5 has 0.5 to 13 meter ground-sampling spatial resolution and is compatible with the ER-2, B-200, Gulfstream, and other airborne platforms. The spectrometer is identical in design to the Earth Surface Mineral Dust Source Investigation (EMIT) spectrometer that flies on the International Space Station (ISS). The AVIRIS-5 started operation in May 2025.

| Dataset | DOI | Short Name | Concept ID |
|---|---|---|---|
| AVIRIS-5 L1B Calibrated Radiance | [10.3334/ORNLDAAC/2483](https://doi.org/10.3334/ORNLDAAC/2483) | AV5_L1B_RDN_2483 | C4076410273-ORNL_CLOUD |
| AVIRIS-5 L2A Orthocorrected Surface Reflectance | [10.3334/ORNLDAAC/2484](https://doi.org/10.3334/ORNLDAAC/2484) | AV5_L2A_RFL_2484 |  C4184090548-ORNL_CLOUD |
| AVIRIS-5 L2B Greenhouse Gas Enhancements | [10.3334/ORNLDAAC/2485](https://doi.org/10.3334/ORNLDAAC/2485) | AV5_L2B_GHG_2485 |C4184090548-ORNL_CLOUD |


## Data Tutorials
- [Search and Discovery of AVIRIS Data](1_AVIRIS_SearchandDiscover.ipynb)
- [Cloud-based Access and Analysis of AVIRIS Data](2_AVIRIS_AccessandAnalysis.ipynb)
- [Working with AVIRIS-5 in ENVI](AVIRIS-5_L2A_ENVI.md)
- [Bulk Download AVIRIS dataset](AVIRIS-C_bulk_download.ipynb)
- [Mapping Invasive Species Using AVIRIS-NG Data](AVIRIS-NG_L3_invasive_species.ipynb)
- [Canopy water content from AVIRIS-NG data](AVIRIS-NG_L3_CWC.ipynb)
- [Search and Download AVIRIS-3 Granules for a Study Area (AVUELO)](../avuelo/AVUELO_2_search_download_granules.ipynb)
- [Extract Quality Spectra of Tree Crowns from AVIRIS-3 Reflectance (AVUELO)](../avuelo/AVUELO_3_AV3_crown_spectra.ipynb)