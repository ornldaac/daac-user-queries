# Understanding AVIRIS-NG data in ENVI format with rotated grid  

Author: ORNL DAAC         
Date: August 21, 2020         
Contact for ORNL DAAC: uso@daac.ornl.gov         
Keywords: Python, GDAL, ENVI, GeoTIFF, Raster, Rotated Grid

## Overview

[AVIRIS-NG](https://aviris-ng.jpl.nasa.gov/) imagery like those collected for the NASA ABoVE Mission (cited below) are distributed in ENVI binary image format. ENVI image analysis software ([Harris Geospatial](https://www.harrisgeospatial.com/Software-Technology/ENVI)) representation of a raster grid allows for a rotated grid such that the pixels are not "north-up". This feature allows the imagery to be analyzed in the **pixel space** without transforming to the **geodetic space**, as would be required in a traditional GIS, and preserves the radiance values as measured by the instrument. The ENVI format rotated grid can cause unfamiliar behavior when the a file is loaded into a GIS (eg. ArcGIS 10.x (as of February 2020)), such as misrepresented X and Y resolutions.

This tutorial explains the concept of the rotated grid from the perspective of a GIS user, the X/Y resolutions in two different (i.e. pixel and geodetic) spaces, and demonstrates how to transform a rotated grid (the pixel space) to north-up (the geodetic space) while minimizing distortion of the underlying data **using GDAL** binary utilities.

**Rotated ENVI files are supported in GDAL version 2.2.0 or greater.**

<img src="images\gdalwarp_result.png" width="750" style="display:block;margin-left: auto; margin-right:auto;">
This image shows a single band of AVIRIS-NG imagery properly displayed within ESRI ArcMap software.

## Dataset

**ABoVE: Hyperspectral Imagery from AVIRIS-NG, Alaskan and Canadian Arctic, 2017-2018**

```
Miller, C.E., R.O. Green, D.R. Thompson, A.K. Thorpe, M. Eastwood, I.B. Mccubbin, W. Olson-duvall, M. Bernas, C.M. Sarture, S. Nolte, L.M. Rios, M.A. Hernandez, B.D. Bue, and S.R. Lundeen. 2019. ABoVE: Hyperspectral Imagery from AVIRIS-NG, Alaskan and Canadian Arctic, 2017-2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1569
```

See the User Guide for a comprehensive description of this dataset:
https://daac.ornl.gov/ABOVE/guides/ABoVE_Airborne_AVIRIS_NG.html


## Prerequisites

**Command line utilities:** GDAL

* `gdal_translate`: https://gdal.org/programs/gdal_translate.html
* `gdalinfo`: https://gdal.org/programs/gdalinfo.html
* `gdalwarp`: https://gdal.org/programs/gdalwarp.html

Download the example granule (L2 reflectance) from the ORNL DAAC data pool at this link:       
https://daac.ornl.gov/daacdata/above/ABoVE_Airborne_AVIRIS_NG/data/ang20170714t213741rfl.tar.gz

Access to this data is free but requires a [NASA Earthdata login](https://urs.earthdata.nasa.gov/) 

## Procedure

Follow this link to the full tutorial:
[AVIRIS-NG_ENVIformat_rotategrid.ipynb](AVIRIS-NG_ENVIformat_rotategrid.ipynb)
