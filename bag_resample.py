#!/usr/bin/env python

from osgeo import gdal, gdalconst
import os
import sys
'''
#highres_file = 'H11760_2m_MLLW_1of10.bag'
highres_file = sys.argv[1]

high = gdal.Open(highres_file, gdalconst.GA_ReadOnly)
high_res = high.GetGeoTransform()[1]
driver = high.GetDriver()
'''
if len(sys.argv) != 2:
    print 'Usage: bag_resample <resolution>'
    sys.exit(1)

out_res = int(sys.argv[1])

file_list = []
for file in os.listdir('.'):
    if file.endswith('.bag'):
        file_list.append( file )
        
for file in file_list:
    src = gdal.Open(file, gdalconst.GA_ReadOnly)
    src_proj = src.GetProjection()
    src_trans = src.GetGeoTransform()
    res = src.GetGeoTransform()[1]
    width = int( src.RasterXSize * res / out_res)
    height = int( src.RasterYSize * res / out_res)
    
    dst_filename = 'resampled_' + os.path.splitext(file)[0] + '.tiff'
    dst = gdal.GetDriverByName('GTiff').Create(dst_filename, width, height, 2, gdalconst.GDT_Float32)
    
    dst.SetProjection(src_proj)
    dst_trans = list(src_trans)
    dst_trans[1] = out_res
    dst_trans[5] = -out_res
    dst.SetGeoTransform(dst_trans)

    gdal.ReprojectImage(src, dst, src_proj, src_proj, gdalconst.GRA_Bilinear)
    del dst





