#/bin/bash
################################################################################
# AUTHOR: TO Hodson 
# simple wrapper for gdal_merge, which merges all resampled rasters in CWD
################################################################################

NAME=$1

FILE_LIST=$(ls | grep resampled | grep tiff$ | sort -n -t _ -k 4)

gdal_merge.py -v -n 0 -of GTiff -o $NAME.tiff $FILE_LIST

#rm *resampled*
