# Carroll-AVIRIS-NG

Information related to Mark Carroll's question about AVIRIS-NG imagery from ABoVE.

## Notes

**Rotated ENVI files are supported in GDAL version 2.2.0 or greater.**

Rotated imagery is not well-supported in ArcMap (not sure if ArcGIS Pro is any better). You probably noticed that ArcMap can't accurately compute the resolution. I've read that (apparently a worldfile helps).

Run this command to translate the ENVI binary image straight to GeoTIFF, preserving the original data types and the image rotation:

## Commands

Run gdalinfo on the ENVI file:

```
[2020-01-24 12:44] $ gdalinfo -nomd ang20170714t213741_corr_v2p9_img
```

Yields:

```
Driver: ENVI/ENVI .hdr Labelled
Files: ang20170714t213741_corr_v2p9_img
       ang20170714t213741_corr_v2p9_img.hdr
Size is 648, 3609
Coordinate System is:
PROJCS["UTM Zone 4, Northern Hemisphere",
    GEOGCS["WGS 84",
        DATUM["WGS_1984",
            SPHEROID["WGS 84",6378137,298.257223563,
                AUTHORITY["EPSG","7030"]],
            AUTHORITY["EPSG","6326"]],
        PRIMEM["Greenwich",0,
            AUTHORITY["EPSG","8901"]],
        UNIT["degree",0.0174532925199433,
            AUTHORITY["EPSG","9122"]],
        AUTHORITY["EPSG","4326"]],
    PROJECTION["Transverse_Mercator"],
    PARAMETER["latitude_of_origin",0],
    PARAMETER["central_meridian",-159],
    PARAMETER["scale_factor",0.9996],
    PARAMETER["false_easting",500000],
    PARAMETER["false_northing",0],
    UNIT["Meter",1]]
GeoTransform =
  581226.666764, 3.86435309248245, 3.479479153066063
  7916192.56364, 3.479479153066063, -3.86435309248245
Corner Coordinates:
Upper Left  (  581226.667, 7916192.564) (156d43'32.15"W, 71d20' 2.93"N)
Lower Left  (  593784.107, 7902246.113) (156d23'28.47"W, 71d12'16.83"N)
Upper Right (  583730.768, 7918447.266) (156d39'11.18"W, 71d21'12.56"N)
Lower Right (  596288.208, 7904500.816) (156d19' 8.05"W, 71d13'26.00"N)
Center      (  588757.437, 7910346.690) (156d31'18.02"W, 71d16'44.86"N)

... 
Band list 
...

```
 















https://gis.stackexchange.com/questions/229952/rotate-envi-hyperspectral-imagery-with-gdal
```
gdalwarp -of envi ang20150422t163638_corr_v1e_img_zero.img ang20150422t163638_corr_v1e_img_zero_rot.img
```


GDAL preserves the image rotation through the metadata such that a typical GIS like ArcMap can still read and manipulate the file. See the columns and rows are the same as in the ENVI image header (752, 8473).

 

The affine transform (geotransform; towards the middle) will give you correct pixel sizes according to these equations:

X = sqrt(GT(1)*GT(1)+GT(2)*GT(2)) = sqrt(1.272792206135786*1.272792206135786 + 1.272792206135785*1.272792206135785) = 1.8

Y = sqrt(GT(4)*GT(4)+GT(5)*GT(5)) = sqrt(1.272792206135785*1.272792206135785 + -1.272792206135786*-1.272792206135786) = 1.8
