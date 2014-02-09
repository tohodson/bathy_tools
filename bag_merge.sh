#/bin/bash

HIGH=$(ls | grep _1of | grep bag$)
NAME=$(cut -f1-2 -d'_' $HIGH)
./bag_upsample.py $HIGH

FILE_LIST=$(ls | grep resampled | grep -v Combined | sort -n -t _ -k 4)

gdal_merge.py -of GTiff -o $NAME.tiff $FILE_LIST

rm *resampled*
