#/bin/bash


NAME=$1

FILE_LIST=$(ls | grep resampled | grep -v Combined | sort -n -t _ -k 4)

gdal_merge.py -of GTiff -o $NAME.tiff $FILE_LIST

rm *resampled*
